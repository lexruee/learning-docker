let mqtt = require('mqtt')
const BROKER_URL = process.env.MQTT_BROKER_URL

if (BROKER_URL == undefined) {
    console.log('Invalid MQTT_BROKER_URL environemnt variable.')
    process.exit(1)
}

let client  = mqtt.connect(BROKER_URL)

client.on('connect',() => {
  client.subscribe('#')
})

client.on('message', (topic, message) => {
  // message is Buffer
  console.log(message.toString())
})


