FROM centos

RUN dnf module install nodejs:16 -y

RUN dnf install python3 -y

RUN ln -s /usr/bin/pip3.6 /usr/bin/pip

RUN pip install --upgrade pip

RUN npm install -g aws-cdk

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

RUN yum install unzip -y

RUN unzip awscliv2.zip

RUN ./aws/install

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
