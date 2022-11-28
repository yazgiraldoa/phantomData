FROM python:3.8

RUN apt-get -y update
RUN apt-get -y upgrade

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get -y install cron

EXPOSE 8080

CMD ["uvicorn", "api:app", "--host=0.0.0.0", "--port=8080"]
