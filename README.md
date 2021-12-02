# RpiServer
Server for the RpiSensor repository.

## Create Docker File and Run
```
docker build -t rpi-server .
```
```
docker run -d -p 3306:3306 rpi-server
```
## DOCKER MYSQL

sudo docker pull mysql:8.0

sudo docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=Pi1 -d mysql:8.0

sudo sudo docker network connect thing_manager_network mysql

mysql_version = 8.0


## NOTES

sudo docker stop rpi_sensor
sudo docker image ls
sudo docker image rm 1d6eff6e2874 --force
sudo docker build -t rpi-server .
sudo docker run -d -p 5000:5000 --name=rpi_sensor --network thing_manager_network rpi-server
sudo docker rm -f 3f011516bc722e9a919d5a2b56021dca4cfbc7725b0e1bb3f1008c424163ef22
sudo docker network inspect thing_manager_network