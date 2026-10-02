Minimax-H3-BF16 - models on network volume only
Dockerfile Path: Minimax-H3-BF16/Dockerfile
Build context: repository root. Include shared volume-tools in Git.
No model downloads during Docker build or worker startup.
Build image contains ComfyUI, custom nodes if required, handler and model checks.
Before inference install models on the volume using NETWORK-VOLUME-SETUP.txt.
Setup Pod command: python3 Minimax-H3-BF16/download_models.py --root /workspace
Attach that SAME populated volume to the endpoint. Serverless mounts it at
/runpod-volume. Missing/incomplete models fail startup with an actionable error.
Model files use models/clip, models/unet, models/vae and models/loras.
These paths are already configured by the base worker. Do not change API filenames.
Queue endpoint; active workers 0; max workers 1; GPUs per worker 1.
Idle timeout 5 seconds. FlashBoot enabled if available. Container disk 30GB
as a starting allocation for runtime/temp outputs; models use separate storage.
GPU recommendations: memory.txt. Client JSON: client-examples/Minimax-H3-BF16.
Network-volume storage is charged even when workers are stopped.
Selecting a volume restricts available workers to its data center.
Cloud volume setup and generation remain untested. No cloud resources created.
