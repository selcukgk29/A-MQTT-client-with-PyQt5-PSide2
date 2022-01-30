import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "localhost"
client = mqtt.Client("faketempclient")
client.connect(mqttBroker,port=1883)

while True:
    randNumber = randrange(17,30)
    client.publish("heater/globaltemp", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(2)