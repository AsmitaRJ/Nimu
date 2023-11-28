FROM python:3.9.10-slim-buster

WORKDIR /usr/src/app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VISTUAL_ENV/bin:$PATH"

RUN python3 -m pip install flask
COPY asmita.py .
ENTRYPOINT FLASK_APP=app flask run --host=0.0.0.0:5000