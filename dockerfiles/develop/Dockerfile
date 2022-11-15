ARG IMAGE
ARG TAG

FROM ${IMAGE}:${TAG}

# 작업에 도움이 되는 프로그램들을 설치한다.
RUN apt-get update -y &&\
    apt-get install -y git &&\
    apt-get install -y vim

# MMOCR 1.x 의존성을 설치한다.
RUN pip install -U openmim &&\
    mim install mmengine &&\
    mim install 'mmcv>=2.0.0rc1'
RUN pip install 'mmdet>=3.0.0rc0'

# MMOCR 1.x 을 설치한다.
RUN cd /root/dev/oss &&\
    git clone https://github.com/open-mmlab/mmocr.git &&\
    mv mmocr src_mmocr &&\
    cd src_mmocr &&\
    git checkout 1.x &&\
    pip install wandb &&\
    pip install -r requirements.txt &&\
    pip install -v -e . &&\
    pip install -r requirements/albu.txt &&\
    pip uninstall opencv-python-headless

# 개발 환경에 사용되는 환경을 구축합니다.
# libgl1-mesa-glx: OpenCV 의존성
RUN apt-get -y install libgl1-mesa-glx

# 작업 디렉터리로 이동한다.
WORKDIR /root/dev/dev/oss/src_mmocr