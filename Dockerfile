FROM python:3

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt || echo "Failed to install requirements"

COPY . .