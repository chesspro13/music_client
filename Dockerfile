FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /
COPY requirements.txt /
RUN apt-get update
RUN apt-get install -y vlc
RUN pip install -r requirements.txt
COPY . /
