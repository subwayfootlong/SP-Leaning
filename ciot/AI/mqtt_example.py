from http import client
import paho.mqtt.client as mqtt

broker="localhost"
client=mqtt.Client("python1")

client.connect(broker)


client.publish("topic","deeznuts")


client.disconnect()