FROM python:3.6

# Create app directory
WORKDIR /

# Install app dependencies
COPY setup.py /

# Bundle app source
COPY outputs /outputs

COPY videos /videos

COPY src /src

RUN apt-get update && apt-get install -y cmake libopenblas-dev liblapack-dev

RUN mkdir build && mkdir dist
RUN python setup.py install

WORKDIR /src

CMD ["python", "elg_demo.py", "--from_video", "../videos/obama_sample.mov", "--record_video", "../videos/obama_sample_output.mov", "--headless" ]