ARG IMAGE
ARG TAG
ARG CUDA_WITHOUT_PATCH_VERSION

FROM ${IMAGE}:${TAG}

RUN apt-get -y \
    install python3-pip
RUN pip3 install \
    torch==1.10.1+cu${CUDA_WITHOUT_PATCH_VERSION} \
    torchvision==0.11.2+cu${CUDA_WITHOUT_PATCH_VERSION} \
    torchaudio==0.10.1 \
    -f https://download.pytorch.org/whl/cu${CUDA_WITHOUT_PATCH_VERSION}/torch_stable.html