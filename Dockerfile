FROM centos

RUN dnf module install nodejs:16 -y

RUN dnf install python3 -y

RUN npm install -g aws-cdk