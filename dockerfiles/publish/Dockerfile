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
RUN mkdir -p /root/dev/oss &&\
    cd /root/dev/oss &&\
    git clone https://github.com/ProtossDragoon/mmocr.git &&\
    mv mmocr src_mmocr &&\
    cd src_mmocr &&\
    git checkout aihub &&\
    pip install tqdm ray wandb &&\
    pip install -r requirements.txt &&\
    pip install -v -e . &&\
    pip install -r requirements/albu.txt &&\
    pip uninstall opencv-python-headless

# 개발 환경에 사용되는 환경을 구축합니다.
# libgl1-mesa-glx: OpenCV 의존성
RUN apt-get -y install libgl1-mesa-glx

# 한글 시각화를 위한 나눔폰트 설치 및 matplotlib 폰트 캐시 제거
RUN apt-get -y install unzip fontconfig &&\
    wget http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip &&\
    unzip NanumFont_TTF_ALL.zip -d NanumFont &&\
    rm -f NanumFont_TTF_ALL.zip &&\
    mv NanumFont /usr/share/fonts/ &&\
    fc-cache -f -v &&\
    rm -rf ~/.cache/matplotlib

# 가중치 파일을 이동시킨다.
WORKDIR /root/dev/oss/src_mmocr/pretrained
COPY pretrained /root/dev/oss/src_mmocr/pretrained

# 스크립트 파일을 이동시킨다.
RUN pip install flask
WORKDIR /root/dev/oss/src_mmocr
COPY *.py /root/dev/oss/src_mmocr/