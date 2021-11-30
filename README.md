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

docker pull mysql:8.0

docker run --name mysql_database -e MYSQL_ROOT_PASSWORD=Pi1 -d mysql:8.0

mysql_version = 8.0