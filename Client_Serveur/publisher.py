import paho.mqtt.client as mqtt
import time
import json
import random
import player

ply = True
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Je participe au jeu")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/testdevice")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Le Serveur me dit")
    data = msg.payload
    print(data)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org")


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
while client.loop() == 0:
    # val=player.asDict()
    # val=json.dumps(val)
    val = 'NOM_PARTICIPANT:VALEUR_DE'  
    client.publish("test/testdevice",val ,0,False)
    time.sleep(1)# sleep for 1 second before next call
client.loop_forever()