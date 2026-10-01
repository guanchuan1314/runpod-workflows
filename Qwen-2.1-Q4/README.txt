Qwen Image 2.1 UC Q4 - RunPod Serverless

Prepared locally. Not deployed or cloud-tested. Docker is unavailable on this PC.
Create accounts at https://console.runpod.io and https://github.com/signup.
Push the Runpod-Serverless folder as the repository root, preserving subfolders.
RunPod Serverless > Import Git Repository > choose repository.
Dockerfile Path: Qwen-2.1-Q4/Dockerfile
Build context: repository root. Base image: verified 5.10.0-base, pinned by digest.
RunPod builds the image; Docker Hub and local Docker are unnecessary.

Suggested settings:
Flex workers; active/min workers 0; max workers 1; GPU count 1.
H100 80GB if desired; container disk 50GB; idle timeout 5 seconds.
Execution timeout 600 seconds; no network volume; FlashBoot enabled if available.
Build downloads ~14.6GB of models once and verifies their SHA256 checksums.
Large container means a longer initial cold start. Build must succeed before testing.
ComfyUI is pinned to locally tested v0.38.0; GGUF extension follows upstream main.

workflow-ui.json: full workflow for ComfyUI / https://comfy.getrunpod.io.
workflow-api.json: executable graph. request.json: complete API request.
Node 452 controls prompt; 458 controls seed/steps; 456 controls dimensions.
Default: 1024 square, 25 steps, CFG 1, Euler/simple, Q4 unrestricted model.

Set RUNPOD_API_KEY and RUNPOD_ENDPOINT_ID locally, then:
python generate.py --prompt "A mountain lake at sunrise"
Use the embedded ComfyUI Python executable if python is not on PATH.
Client sends /run, polls /status, and saves images into generated/job-id/.
Never commit API keys. Interrupted/timed-out client does not cancel the cloud job.
Check/cancel that job in the RunPod console.

GPU compute is zero after all workers stop with active workers 0.
Startup, generation, idle timeout and allocated container disk are billed.
Persistent network volumes would cost money even with no requests; none here.
Review the model license before commercial use. Publisher's unrestricted claim
does not guarantee every requested output.
