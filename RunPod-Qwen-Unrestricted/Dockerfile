FROM runpod/worker-comfyui:5.11.0-base
RUN cd /comfyui && git fetch --tags && git checkout v0.38.0 && pip install -r requirements.txt
RUN git clone https://github.com/leejet/ComfyUI-GGUF.git /comfyui/custom_nodes/ComfyUI-GGUF && pip install -r /comfyui/custom_nodes/ComfyUI-GGUF/requirements.txt
COPY download_models.py /download_models.py
RUN python /download_models.py
RUN cd /comfyui && python main.py --quick-test-for-ci --cpu
