FROM python:3.11.2-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Install development dependencies
RUN pip install --upgrade twine
