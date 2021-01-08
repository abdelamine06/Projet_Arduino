import paho.mqtt.client as mqtt
import json
import time
import random
import game


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/testdevice")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message recu Client")
    data = msg.payload
    if data == b'playing' : # tentative d'envoie d'un score 
        client.publish("test/testdevice", "5",0,False)
    print(data)
#se ",data["house_id"]," reported Temperature=",data["Temperature"],"C Humidity=",data["Humidity"],"%"," Current =",data["Current"]

client = mqtt.Client(client_id = "Paul")
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org")
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
i = 0

# envoie 3 clients différents pour les faire entré dans le dict
while client.loop() == 0:
    client.publish("test/testdevice","Paul ",0,False)
    time.sleep(1)# sleep for 1 second before next call


client.loop_forever()
