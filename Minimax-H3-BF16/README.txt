MiniMax H3 BF16 generator + BF16 Heretic encoder
Dockerfile Path: Minimax-H3-BF16/Dockerfile
Build context: repository root. See memory.txt.
Client workflows: client-examples/Minimax-H3-BF16.

Models alone total ~99.5GB, exceeding the previously checked 80GB GitHub
build image limit. Do not deploy this model-baked Dockerfile through GitHub.
Requires external model storage or a verified alternative build/registry route.
Persistent storage can incur costs while workers are off. Cloud setup untested.
