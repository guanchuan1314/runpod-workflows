"""Run once on a setup Pod with the network volume mounted. No GPU required."""
import argparse
import hashlib
import json
import pathlib
import urllib.request

FOLDERS = {'text_encoders': 'clip', 'diffusion_models': 'unet', 'vae': 'vae', 'loras': 'loras'}

def checksum(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def install(manifest, root):
    if not root.is_dir():
        raise RuntimeError('Volume mount must already exist; check --root')
    for model in json.loads(manifest.read_text(encoding='utf-8-sig')):
        dest = root / 'models' / FOLDERS[model['folder']] / pathlib.PurePosixPath(model['file']).name
        dest.parent.mkdir(parents=True, exist_ok=True)
        lock = dest.with_name(dest.name + '.install-lock')
        try:
            lock.mkdir()
        except FileExistsError:
            raise RuntimeError(f'Another installer or stale lock exists: {lock}')
        try:
            if dest.exists():
                if checksum(dest) != model['sha256']:
                    raise RuntimeError(f'Existing model checksum mismatch: {dest}; inspect before replacing')
                print('Verified existing:', dest.name, flush=True)
                continue
            partial = dest.with_name(dest.name + '.part')
            offset = partial.stat().st_size if partial.exists() else 0
            headers = {'Range': f'bytes={offset}-'} if offset else {}
            url = f"https://huggingface.co/{model['repo']}/resolve/main/{model['file']}"
            request = urllib.request.Request(url, headers=headers)
            print('Downloading:', dest.name, 'resume bytes:', offset, flush=True)
            with urllib.request.urlopen(request, timeout=120) as response:
                append = offset > 0 and response.status == 206
                if append and not response.headers.get('Content-Range', '').startswith(f'bytes {offset}-'):
                    raise RuntimeError('Unexpected download range')
                with partial.open('ab' if append else 'wb') as out:
                    while chunk := response.read(8 * 1024 * 1024):
                        out.write(chunk)
            if model.get('size') and partial.stat().st_size != model['size']:
                raise RuntimeError(f'Size mismatch: {partial}')
            if checksum(partial) != model['sha256']:
                raise RuntimeError(f'Checksum mismatch: {partial}; inspect partial file before retry')
            partial.replace(dest)
            print('Installed:', dest.name, flush=True)
        finally:
            lock.rmdir()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', type=pathlib.Path, required=True)
    parser.add_argument('--root', type=pathlib.Path, required=True, help='/workspace on a setup Pod; /runpod-volume on Serverless')
    args = parser.parse_args()
    install(args.manifest, args.root)
