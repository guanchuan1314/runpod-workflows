MiniMax H3 Heretic - RunPod Serverless preparation

Dockerfile Path: Minimax-H3-INT8/Dockerfile
Build context: Runpod-Serverless repository root.
Queue endpoint. Active workers 0, max workers 1, GPUs per worker 1.
Start with 96GB GPU tier; 80GB is a possible alternative to benchmark.
Container disk 100GB, idle timeout 5 seconds, execution timeout 1800 seconds.
No network volume. FlashBoot enabled if available.

Includes INT8 ConvRot diffusion model and 32B Heretic text encoder,
video/audio VAEs and optional Turbo LoRA. Approximately 55GB of model files.
Higher-resolution/longer videos increase runtime memory; GPU recommendation
is a planning estimate, not cloud-tested. Default API examples use short,
low-resolution clips already tested locally, with standard 20-step sampling.

models.json is a BUILD manifest, required by download_models.py; keep it here.
Inference workflow JSON files are separate under client-examples/Minimax-H3-INT8.
Full UI workflows retain the original layout and optional Turbo branch.
The API examples are minimal locally tested graphs, with Turbo disabled.
For image-to-video, send input.images containing the reference image as Base64
with a name matching the LoadImage node's image filename.
Send the request JSON to /run and poll /status/JOB_ID from your backend.
SaveVideo outputs use output.images entries even though their files are MP4.
Default worker returns Base64; decode as MP4. Keep S3 disabled until video
upload handling is separately verified. Long video outputs may require a
custom object-storage handler to avoid response-size limits.

Not deployed or cloud-tested. No models downloaded again on this PC.
The large build must download ~55GB within RunPod's Docker build time limit;
if it exceeds the limit, prebuild/push to a registry or use persistent storage.
Compute is billed during startup, execution and idle timeout. Container disk
is billed while allocated; persistent storage would have separate charges.
