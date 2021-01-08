import paho.mqtt.client as mqtt
import time
import json
import random
import game


game = game.game(1)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/testdevice")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message recu SERVEUR")
    data = msg.payload
    if data !=  b'wait' and data != b'playing' : # on evite de les rentrer dans le dict c'est moche mais ca passe
        game.setPlayer({str(msg.payload) : { 'res' : 0}})
    if game.getLenght() == game._nbPlayerNeeded : # nombre de joueur requis; on veut recup les dé maintenant
        print(game.asDict())
        game._status = "playing"
    print(data)
    

client = mqtt.Client(client_id="Paul Serv")
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org");


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
while client.loop() == 0:
    #0-1000 Deira Dubai
    #1000-1050 Abu Shagara
    #1050-1150 University City
    #data = json.dumps(game.asDict())
    if game._status == "wait" :
        client.publish("test/testdevice", "wait",0,False)
    if game._status == "playing" : 
        client.publish("test/testdevice", "playing",0,False)

    time.sleep(1)# sleep for 1 second before next call
