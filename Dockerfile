FROM python:3.8-buster

WORKDIR /src
ADD requirements.txt /src
RUN pip install -r requirements.txt

ADD src /src/app

WORKDIR /src/app

CMD ["python", "/src/main.py"]
