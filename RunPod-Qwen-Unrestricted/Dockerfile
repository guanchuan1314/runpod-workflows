FROM runpod/worker-comfyui:5.10.0-base@sha256:e9d18d3db15839ebb10c10c824109fc2956f31ef7bf21916220c008855b0d538
RUN cd /comfyui && git fetch --tags && git checkout v0.38.0 && pip install -r requirements.txt
RUN git clone https://github.com/leejet/ComfyUI-GGUF.git /comfyui/custom_nodes/ComfyUI-GGUF && pip install -r /comfyui/custom_nodes/ComfyUI-GGUF/requirements.txt
COPY RunPod-Qwen-Unrestricted/download_models.py /download_models.py
RUN python /download_models.py
RUN cd /comfyui && python main.py --quick-test-for-ci --cpu
