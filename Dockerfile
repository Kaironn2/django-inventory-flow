FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install build setuptools wheel
RUN pip install .

EXPOSE 8000

CMD python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000
