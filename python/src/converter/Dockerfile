FROM python:3.10-slim-bullseye

RUN apt-get update

RUN apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential ffmpeg \
  && pip install --no-cache-dir --upgrade pip


WORKDIR /app
COPY req.pip /app


RUN pip install --no-cache-dir --requirement /app/req.pip

COPY . .

CMD ["python3", "consumer.py"]

