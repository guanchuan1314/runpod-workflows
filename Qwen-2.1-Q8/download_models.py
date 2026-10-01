import hashlib
import pathlib
import urllib.request

models = [
    ('diffusion_models', 'abenzerps/Qwen-Image-2.1-Uncensored-GGUF', 'qwen-image-2.1-UC-Q8_0.gguf', 'cde456c72ea3ecebfc1be783300e972711d875e0c5f1bed33d42b66b156affa8'),
    ('text_encoders', 'Comfy-Org/Qwen-Image-2.1', 'text_encoders/qwen3vl_8b_int8_convrot.safetensors', '8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f'),
    ('vae', 'Comfy-Org/Qwen-Image-2.1', 'vae/qwen_image_2.1_vae_bf16.safetensors', 'bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9'),
]
for folder, repo, file, expected in models:
    dest = pathlib.Path('/comfyui/models') / folder / pathlib.Path(file).name
    dest.parent.mkdir(parents=True, exist_ok=True)
    print('Downloading', dest.name, flush=True)
    digest = hashlib.sha256()
    with urllib.request.urlopen(f'https://huggingface.co/{repo}/resolve/main/{file}', timeout=120) as src, dest.open('wb') as out:
        while chunk := src.read(8 * 1024 * 1024):
            out.write(chunk)
            digest.update(chunk)
    if digest.hexdigest() != expected:
        raise RuntimeError(f'Checksum failed: {dest.name}')
