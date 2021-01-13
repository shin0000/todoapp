FROM ubuntu

MAINTAINER shinji

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install sudo
RUN apt-get -y install vim
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install curl
RUN sudo apt-get install -y python-dev
RUN sudo apt-get install -y libpq-dev
RUN pip3 install -U psycopg2

# ADD ./api_test2/ /api_test2/

COPY ./startup.sh /startup.sh
COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt
CMD sh /startup.sh

EXPOSE 8000