FROM python:3.11.2-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
