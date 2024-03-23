FROM ghcr.io/merklebot/hackathon-arm-image:master as build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG TARGETPLATFORM
ARG BUILDPLATFORM
ARG TARGETOS
ARG TARGETARCH

ARG Version
ARG GitCommit
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM" 


COPY requirements.txt requirements.txt
RUN python3.8 -m pip install -r requirements.txt
RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev -y \
        && python3.8 -m pip install pyaudio
COPY . .

CMD ["python3.8", "main.py"]
