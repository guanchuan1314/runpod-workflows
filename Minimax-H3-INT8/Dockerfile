FROM runpod/worker-comfyui:5.10.0-base@sha256:e9d18d3db15839ebb10c10c824109fc2956f31ef7bf21916220c008855b0d538
RUN cd /comfyui && git fetch --tags && git checkout v0.38.0 && pip install -r requirements.txt
COPY Minimax-H3-INT8/models.json /models.json
COPY Minimax-H3-INT8/download_models.py /download_models.py
RUN python /download_models.py
RUN cd /comfyui && python main.py --quick-test-for-ci --cpu
