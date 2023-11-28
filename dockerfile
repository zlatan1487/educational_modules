FROM python:3

WORKDIR /code

COPY ./requirements.txt  /code

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code

CMD ["python", "manage.py", "runserver", "--bind", "0.0.0.0:8000"]