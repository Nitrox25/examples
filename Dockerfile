FROM python:3.9.4-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

#COPY . /code/
COPY requirements.txt /code
RUN pwd; ls -l
RUN pip install -r requirements.txt
ENV HOST_NAME localhost
#ENV FRONT_NAME https://demo.megadex.com/

ENTRYPOINT []
SHELL ["/bin/bash", "-c"]
CMD pwd ; ls  \
    && sleep 60 \
    && py.test /storage/ ; \
    sleep 3600

#- py.test -n=15  --dist=loadfile  --alluredir=./allure-results-akbars  akbars
#  py.test -n=25  --dist=loadfile  --alluredir=./allure-results-unic  unicredit