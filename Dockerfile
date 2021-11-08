#FROM python:3.7.12
FROM rappdw/docker-java-python:openjdk1.8.0_171-python3.6.6

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /usr/src/app/

CMD [ "python3", "manager.py" ]
