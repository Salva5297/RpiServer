# RpiServer
Server for the RpiSensor repository.

## Create Docker File and Run
```
docker build -t rpi-server .
```
```
docker run -d -p 3306:3306 rpi-server
```

mysql 8.0