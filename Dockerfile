FROM python:3.8.2

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED 1
ENV DEBUG = False

RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic
RUN make migrate all

CMD gunicorn almox.wsgi:application --reload