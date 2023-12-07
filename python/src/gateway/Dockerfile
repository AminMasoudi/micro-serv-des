FROM python:3.10-slim-bullseye

RUN apt-get update\
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential \
  && pip install --no-cache-dir --upgrade pip


WORKDIR /app
COPY req.pip /app
RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`

RUN pip install --no-cache-dir --requirement /app/req.pip
COPY . .
EXPOSE 8080 
CMD ["python3", "server.py"]

