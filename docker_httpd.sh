echo "-----------------------This is for Configuring Apache WebServer inside Docker Container----------------------"
echo "----------------------Prerequisite for this that you have Docker installed in the system-------------------------"

echo "----------------------------------Removing container nammed 'webserver' if already exixts---------------------------------"
docker rm -f webserver

echo "----------------------------------Launching Docker Container with the Centos image and Expose it to port 8080---------------------------------"
docker run -dit --name webserver -p 8080:80 centos:latest

echo "----------------------------------Installing Apache webserver & net-tools inside container---------------------------------"
docker exec -i webserver yum install httpd net-tools -y

echo "----------------------------------Starting httpd service---------------------------------"
docker exec -i webserver /usr/sbin/httpd

echo "----------------------------------Confirming that service is running or not---------------------------------"
docker exec -i webserver netstat -tnlp

echo "---------------------------------Copying web pages in Conainer --------------------------------"
docker cp index.html webserver:/var/www/html
