FROM python:3.10.6-buster

USER root
RUN apt-get update
RUN apt-get install python3-opencv -y

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# docker build -t blur-image:1.0 .
# docker run -p 8000:8000 --name blur-image blur-image:1.0