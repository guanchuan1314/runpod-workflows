Qwen Image 2.1 UC Q8 - RunPod Serverless

Prepared locally. Not deployed or cloud-tested. Docker is unavailable on this PC.
Create accounts at https://console.runpod.io and https://github.com/signup.
Push the Runpod-Serverless folder as the repository root, preserving subfolders.
RunPod Serverless > Import Git Repository > choose repository.
Dockerfile Path: Qwen-2.1/Dockerfile
Build context: repository root. Base image: verified 5.10.0-base, pinned by digest.
RunPod builds the image; Docker Hub and local Docker are unnecessary.

Suggested settings:
Flex workers; active/min workers 0; max workers 1; GPU count 1.
48GB GPU recommended; container disk 50GB; idle timeout 5 seconds.
Execution timeout 600 seconds; no network volume; FlashBoot enabled if available.
Build downloads ~17.6GB of models once and verifies their SHA256 checksums.
Large container means a longer initial cold start. Build must succeed before testing.
ComfyUI is pinned to locally tested v0.38.0; GGUF extension follows upstream main.

Client examples are stored separately in client-examples/Qwen-2.1.
That folder contains the API graph, full request, UI workflow and local test helper.
Node 452 controls prompt; 458 controls seed/steps; 456 controls dimensions.
Default: 1024 square, 25 steps, CFG 1, Euler/simple, Q8 unrestricted model.

Call from your web app backend: POST /v2/ENDPOINT_ID/run with client-examples/Qwen-2.1/request.json contents.
Change node 452 inputs.prompt before submission; poll /status/JOB_ID for results.
Keep the API key on your backend. The separate Call-Qwen.ps1 is an optional local test helper.
The container uses the base image's built-in RunPod handler.

GPU compute is zero after all workers stop with active workers 0.
Startup, generation, idle timeout and allocated container disk are billed.
Persistent network volumes would cost money even with no requests; none here.
Review the model license before commercial use. Publisher's unrestricted claim
does not guarantee every requested output.
