FROM python:2.7.12-alpine
MAINTAINER Rama Bramantara "rama@onebitmedia.com"

# Dependencies
RUN apk add --update bash && rm -rf /var/cache/apk/*
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Workspace
COPY . /app
WORKDIR /app
COPY docker/entrypoint.sh /app/entrypoint.sh
COPY docker/test-unit.sh /app/test-unit.sh

ENTRYPOINT ["/app/entrypoint.sh"]
