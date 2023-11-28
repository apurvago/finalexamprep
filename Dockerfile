FROM python:3.9.10-slim-buster

WORKDIR /usr/src/app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m pip install flask
RUN python3 -m pip install gunicorn

COPY basicf.py .
ENTRYPOINT FLASK_APP=basicf flask run --host=0.0.0.0
EXPOSE 8000