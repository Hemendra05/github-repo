FROM ubuntu

RUN apt update &&\
    apt upgrade &&\
    apt install curl -y &&\
    curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh &&\
    bash nodesource_setup.sh &&\
    apt install nodejs -y &&\
    apt install python3-pip -y &&\
    apt install unzip -y &&\
    apt install jq -y &&\
    npm install -g aws-cdk

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

RUN unzip awscliv2.zip

RUN ./aws/install

RUN pip install wheel

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
