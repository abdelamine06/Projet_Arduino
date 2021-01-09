import paho.mqtt.client as mqtt
import time
import json
import random
from pyduino import *
import math


ply = True
value = 0
mode = "MODE" # A remplacer par le mode de lancement

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

def lance_des():
    value = random.randint(1,6)
    i = 2
    while(i<value+2):
        a.digital_write(i,1) # turn LED on
        i+=1

    return value

def thermistor(v):

    Temp = 10000.0 * ((1024.0/v)-1)
    Temp = 1 / ( 0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp )) * Temp )
    Temp = Temp-273.15
    Temp = ( Temp*9.0 )/5.0 + 32.0

    return Temp

def setup_ultrason():
    a.set_pin_mode(8,'I')
    a.set_pin_mode(9,'O')

def setup_bouton():
    a.set_pin_mode(9,'I')


def joue():

    if(mode == "ultrason"):
        a.digital_write(9, 0)
        time.sleep(0.000003)#delayMicroseconds(3)
        a.digital_write(9, 1)
        time.sleep(0.00001)#delayMicroseconds(10)
        a.digital_write(9, 0)
        stop = 0
        v = 0
        while stop == 0:
            if(a.digital_read(8) == 1):
                debut=time.time()
                v = 1
            if (a.digital_read(8) == 0 and v == 1):
                temps = time.time() - debut
                stop = 1
                v = 0
        distance = temps*100*0.034/2
        if(distance<5):
            value = lance_des()
            return value

    elif(mode == "bouton"):
        if(a.digital_read(9) == 1):
            value = lance_des()
            return value

    elif(mode == "lumiere"):
            luminosite1 = a.analog_read(0)
            print(luminosite1)
            time.sleep(0.1)
            luminosite2 = a.analog_read(0)
            print(luminosite2)
            if( abs(luminosite2-luminosite1) > 10  ):
                value = lance_des()
                return value

    elif(mode == "temperature"):
        time.sleep(1)
        val1 = a.analog_read(0)
        print(val1)
        val2 = a.analog_read(0)
        if(abs(val1-val2) > 1 ):
            value = lance_des()
            return value

    return 0


print('[Arduino] Establishing connection to Arduino...')

# if your arduino was running on a serial port other than '/dev/ttyACM0/'
# declare: a = Arduino(serial_port='/dev/ttyXXXX')
a = Arduino(serial_port='/dev/ttyACM3')

# sleep to ensure ample time for computer to make serial connection
time.sleep(3)
print('[Arduino] established!')

# initialize the digital pin as output
#a.set_pin_mode(3,'O')

if(mode == "ultrason"):
    print("je lance le des Mode Ultrason !!!!")
    setup_ultrason()

elif(mode == "bouton"):
    print("je lance le des Mode Bouton !!!!")
    setup_bouton()

elif(mode == "lumiere"):
    print("je lance le des Mode Lumiere !!!!")

elif(mode == "temperature"):
    print("je lance le des Mode Temperature !!!!")

    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org")



# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
while client.loop() == 0:

    value = joue()
    # val=player.asDict()
    # val=json.dumps(val)
    val = 'NOM_PARTICIPANT:'+str(value)  # A remplacer par le nom du joueur 
    client.publish("test/testdevice",val ,0,False)
    time.sleep(1)# sleep for 1 second before next call
client.loop_forever()