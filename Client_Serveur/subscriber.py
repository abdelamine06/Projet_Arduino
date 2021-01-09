import paho.mqtt.client as mqtt
import json
import time
import random
import game

begin = True;
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global begin
    while begin == True:
        print("Debut de la partie!")
        begin = False;
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/testdevice")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = msg.payload
    if data == b'playing' : # tentative d'envoie d'un score 
        client.publish("test/testdevice", "5",0,False)
    print(data)
    global begin
    while begin == False:
        time.sleep(5);
        print("Qui va jouer?")
        begin = True;
    
#se ",data["house_id"]," reported Temperature=",data["Temperature"],"C Humidity=",data["Humidity"],"%"," Current =",data["Current"]

client = mqtt.Client(client_id = "Paul")
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org")
client.loop_forever()
