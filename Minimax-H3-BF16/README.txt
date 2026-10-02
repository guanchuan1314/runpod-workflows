Minimax-H3-BF16 - models included in the registry container image
Dockerfile Path: Minimax-H3-BF16/Dockerfile
Build context: repository root. Include shared model-tools in Git.
Build downloads and SHA-256 verifies all models from models.json.
Installed paths: /comfyui/models/clip, unet, vae and loras.
The inherited RunPod worker starts ComfyUI and the Queue API handler.
No network volume is required. No model downloads at worker startup.
Workflow JSON stays in client-examples/Minimax-H3-BF16; send input.workflow via API.

Build and push:
  docker build --platform linux/amd64 -f Minimax-H3-BF16/Dockerfile -t docker.io/guanchuan93/runpod-comfyui:minimax-h3-bf16-<version> .
  docker push docker.io/guanchuan93/runpod-comfyui:minimax-h3-bf16-<version>
Use an immutable version tag or digest when deploying the image to RunPod.
Select Deploy from a Docker image and use the registry image address.
For a private image, configure registry pull credentials in RunPod.
Endpoint name: Minimax-H3-BF16. Queue; active workers 0; max workers 1; GPUs per worker 1.
Idle timeout 5 seconds. FlashBoot enabled if available.
Suggested container disk: 150GB, allowing software, weights and temporary media.
GPU memory recommendations: memory.txt and GPU-options.txt when present.

Model weights: 99.50GB. Suggested builder free disk: 350GB.
The builder needs room for the base image, models, layers and image export.
MiniMax needs a builder outside the previously failing RunPod GitHub build path.
Earlier builds encountered image-size/time limits; registry deployment still
requires a successful large-image build and pull. Cold starts may be longer.
Registry image built, model checksums verified, uploaded and deployed on
2026-10-02. Cloud T2V returned decodable MP4 video and audio on an H200 SXM.
See DEPLOYMENT-STATUS.txt for the short smoke-test scope and observed timings.
See CONTAINER-REGISTRY-SETUP.txt for deployment details.
