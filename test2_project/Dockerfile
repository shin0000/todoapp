FROM ubuntu

MAINTAINER shinji

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install sudo
RUN apt-get -y install vim
RUN apt-get -y install curl
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN apt-get remove cmdtest
RUN apt-get remove yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update  
RUN apt-get install yarn
RUN yarn install
RUN yarn global add create-react-app
RUN yarn add axios
RUN yarn add http-proxy-middleware

COPY ./startup.sh /startup.sh

EXPOSE 3000