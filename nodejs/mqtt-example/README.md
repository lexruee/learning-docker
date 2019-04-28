# MQTT.js Example

* MQTT Broker: `mqtt://10.0.0.70:1883`


## Build the image

``` 
docker build -t mqtt-js-test .
```

## Running the image

``` 
docker run --rm -it -e MQTT_BROKER_URL=mqtt://10.0.0.70:1883 \ 
    --name mqtt-js-test mqtt-js-test
docker stop mqtt-js-test
```


## Docker compose

Build the image:

``` 
docker-compose build
```

Run the container:

``` 
docker-compose up
```