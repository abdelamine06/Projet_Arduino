import paho.mqtt.client as mqtt
import time
import json
import random
import game
import player
from pyduino import *
import math




if __name__ == '__main__':

    game = game.game(1)
    value =0

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

        if(game._mode == "ultrason"):
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

        elif(game._mode == "bouton"):
            if(a.digital_read(9) == 1):
                value = lance_des()
                return value

        elif(game._mode == "lumiere"):
              luminosite1 = a.analog_read(0)
              print(luminosite1)
              time.sleep(0.1)
              luminosite2 = a.analog_read(0)
              print(luminosite2)
              if( abs(luminosite2-luminosite1) > 10  ):
                  value = lance_des()
                  return value

        elif(game._mode == "temperature"):
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
    a = Arduino(serial_port='/dev/ttyACM0')

    # sleep to ensure ample time for computer to make serial connection
    time.sleep(3)
    print('[Arduino] established!')

    # initialize the digital pin as output
    #a.set_pin_mode(3,'O')
    player = player.player(1)


    client = mqtt.Client(client_id="Paul Serv")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("test.mosquitto.org")

    #time.sleep(1)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.

    if(game._mode == "ultrason"):
        print("je lance le des Mode Ultrason !!!!")
        setup_ultrason()

    elif(game._mode == "bouton"):
        print("je lance le des Mode Bouton !!!!")
        setup_bouton();

    elif(game._mode == "lumiere"):
        print("je lance le des Mode Lumiere !!!!")

    elif(game._mode == "temperature"):
        print("je lance le des Mode Temperature !!!!")


    while  value == 0 :
        value = joue()

    print("Valeur recupere : ", value)

    while client.loop() == 0 :
        if game._status == "wait" :
            client.publish("test/testdevice", "wait",0,False)
        if game._status == "playing" :
            client.publish("test/testdevice", "playing",0,False)


            time.sleep(1)
    print ('CLOSING...')
    a.close()
