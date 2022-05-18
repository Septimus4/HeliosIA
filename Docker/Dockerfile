FROM tensorflow/tensorflow:latest-gpu

WORKDIR /tmp

RUN apt-get update -y \
&& apt-get upgrade -y \
&& apt-get install --no-install-recommends -y python3 \
&& apt-get install -y python3-pip \
&& python3 -m pip install --upgrade pip \
&& apt-get install -y apt-utils libsm6 libxext6 libxrender-dev \
&& apt-get install -y git \
&& apt-get install -y wget

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

WORKDIR /home/training

CMD /bin/bash
