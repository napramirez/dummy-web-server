FROM python:3-alpine

WORKDIR /app

COPY dummy-web-server.py /app

CMD ["/usr/local/bin/python3", "/app/dummy-web-server.py"]
