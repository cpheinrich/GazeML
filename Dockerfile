FROM python:3.6

# Create app directory
WORKDIR /

# Install app dependencies
COPY setup.py /

# Bundle app source
COPY outputs /outputs

COPY videos/tracking_sample.mov /src/videos/tracking_sample.mov

VOLUME src/videos

COPY src /src

RUN apt-get update && apt-get install -y cmake libopenblas-dev liblapack-dev

RUN mkdir build && mkdir dist
RUN python setup.py install

WORKDIR /src

ENTRYPOINT ["python", "inference.py"]

CMD ["--from_video", "/src/videos/tracking_sample.mov"]