ARG IMAGE
ARG TAG
ARG CUDA_VERSION

FROM ${IMAGE}:${TAG}

RUN pip3 install -y \
    torch==1.10.1+cu${CUDA_VERSION} \
    torchvision==0.11.2+cu${CUDA_VERSION} \
    torchaudio==0.10.1 \
    -f https://download.pytorch.org/whl/cu${CUDA_VERSION}/torch_stable.html