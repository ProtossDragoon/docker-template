ARG IMAGE
ARG TAG

FROM ${IMAGE}:${TAG}

# 작업에 도움이 되는 프로그램들을 설치한다.
RUN apt-get update -y &&\
    apt-get install -y git &&\
    apt-get install -y vim

# 작업 디렉터리를 생성한다.
RUN mkdir -p /root/dev
WORKDIR /root/dev