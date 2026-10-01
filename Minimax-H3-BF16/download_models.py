import hashlib
import json
import pathlib
import urllib.request

for model in json.loads(pathlib.Path('/models.json').read_text()):
    dest = pathlib.Path('/comfyui/models') / model['folder'] / pathlib.Path(model['file']).name
    dest.parent.mkdir(parents=True, exist_ok=True)
    print('Downloading', dest.name, flush=True)
    digest = hashlib.sha256()
    url = f"https://huggingface.co/{model['repo']}/resolve/main/{model['file']}"
    with urllib.request.urlopen(url, timeout=120) as src, dest.open('wb') as out:
        while chunk := src.read(8 * 1024 * 1024):
            out.write(chunk)
            digest.update(chunk)
    if dest.stat().st_size != model['size'] or digest.hexdigest() != model['sha256']:
        raise RuntimeError(f'Model verification failed: {dest.name}')
