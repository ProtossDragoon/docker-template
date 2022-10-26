ARG IMAGE
ARG TAG

FROM ${IMAGE}:${TAG}

# ssh 환경을 구축한다.
RUN apt-get update -y && \
    apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# 루트로의 패스워드(패스워드: root) 기반 login 을 허용시킨다.
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# 위 방법으로만은 로그인이 되지 않을 때 시도해본다. 
# 로그인 시 /etc/pam.d 기반의 인증(UsePAM)을 사용하지 않도록 만든다.
# RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

# 포트를 개방한다.
EXPOSE 22