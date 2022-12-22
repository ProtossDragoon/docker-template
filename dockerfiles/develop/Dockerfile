ARG IMAGE
ARG TAG

FROM ${IMAGE}:${TAG}

# GitLab
RUN mkdir -p /root/.ssh
ADD id_rsa /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts &&\
    ssh-keyscan 192.168.200.20 >> /root/.ssh/known_hosts
RUN chmod 400 ~/.ssh/id_rsa &&\
    chmod 400 ~/.ssh/known_hosts

# 작업에 도움이 되는 프로그램들을 설치한다.
RUN apt-get update -y &&\
    apt-get install -y git &&\
    apt-get install -y vim

# MMOCR 1.x 의존성을 설치한다.
RUN pip install -U openmim &&\
    mim install mmengine &&\
    mim install 'mmcv>=2.0.0rc1'
RUN pip install 'mmdet>=3.0.0rc0'

# F1 Score 도구를 설치한다.
RUN mkdir -p /root/dev/oss/OCRE2EHMean &&\
    cd /root/dev/oss/OCRE2EHMean &&\
    echo $PWD &&\
    git clone git@192.168.200.20:ailab/AiSolutionLabMiniTask.git . &&\
    git checkout aihub &&\
    make install &&\
    cd ..

# MMOCR 1.x 을 설치한다.
RUN mkdir -p /root/dev/oss/src_mmocr &&\
    cd /root/dev/oss/src_mmocr &&\
    echo $PWD &&\
    git clone git@192.168.200.20:ailab/ocr/aihub-ocr-mmocr.git . &&\
    git checkout aihub &&\
    pip install tqdm ray wandb &&\
    pip install -r requirements.txt &&\
    pip install -v -e . &&\
    pip install -r requirements/albu.txt &&\
    pip uninstall opencv-python-headless &&\
    cd ..

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
WORKDIR /root/dev
COPY *.sh /root/dev/
