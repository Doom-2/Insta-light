
FROM python:3.10-slim

ENV HOME /

WORKDIR $HOME

ENV FLASK_APP=run.py

RUN apt-get update -y  \
    && apt-get install -y --no-install-recommends curl \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt .

RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .

CMD gunicorn --config gunicorn.conf.py run:app