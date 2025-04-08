# 베이스 이미지
FROM ubuntu:22.04

# 메타데이터 추가
LABEL maintainer="YB dbqls3698@naver.com"

# 시스템 업데이트
RUN apt update -y && \
       apt install -y sudo passwd openssh-server wget && \
       apt install -y nano net-tools && \
       apt install -y iputils-ping openjdk-8-jdk python3-pip && \
       apt clean && \
       rm -rf /var/lib/apt/lists/*

# 계정생성 및 세팅
RUN groupadd pkyb && useradd -m -d /home/pkyb -s /bin/bash -g pkyb -G sudo pkyb && \
       echo "pkyb:1234" | chpasswd && \
       mkdir -p /home/pkyb/.ssh && \
       chown -R pkyb:pkyb /home/pkyb && \
       echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/pkyb/.bashrc && \
       echo "export PATH=$PATH:/home/pkys/.local/bin" >> /home/pkys/.bashrc && \
       chown pkyb:pkyb /home/pkyb/.bashrc && \
       mkdir -p /var/run/sshd && \
       echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
       echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

# 사용자 변경
USER pkyb

# 작업환경 변경
WORKDIR /home/pkyb

# pip 업그레이드 및 주피터랩 설치
RUN pip install --upgrade pip && pip install jupyterlab

# ssh 서버 실행 및 주피터랩 가동(외부접속가능)
CMD ["/bin/bash","-c","service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --port=8888 --allow-root --FileContentsManager.delete_to_trash=False"]