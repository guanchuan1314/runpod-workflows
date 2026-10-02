"""Fast startup presence check; full SHA256 verification happens during install."""
import json
import pathlib

folders = {'text_encoders': 'clip', 'diffusion_models': 'unet', 'vae': 'vae', 'loras': 'loras'}
missing = []
for model in json.loads(pathlib.Path('/models.json').read_text()):
    path = pathlib.Path('/runpod-volume/models') / folders[model['folder']] / pathlib.PurePosixPath(model['file']).name
    if not path.is_file() or path.stat().st_size == 0 or (model.get('size') and path.stat().st_size != model['size']):
        missing.append(str(path))
if missing:
    raise SystemExit('Network-volume models missing/incomplete. Run the installer on the attached volume first:\n' + '\n'.join(missing))
print('Network-volume model presence check passed', flush=True)
