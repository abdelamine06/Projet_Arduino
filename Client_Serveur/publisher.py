import paho.mqtt.client as mqtt
import time
import json
import random
import game
import player
from pyduino import *



if __name__ == '__main__':

    game = game.game(1)
    debut=time.time()


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
  

    def joue():

        if(game._mode == "ultrason"):
            a.set_pin_mode(8,'O')
            a.set_pin_mode(9,'I')
            a.digital_write(8, 0)
            time.sleep(1)
            a.digital_write(9, 1)

            temps = time.time() - debut
            distance = temps*0.034/2

            print("la distance est : ", distance)
            
            if(distance<5):
                print("je lance le des Mode ultrason !!!!")
                value = lance_des()

                return value

        if(game._mode == "button"): 
            
            a.set_pin_mode(9,'I')

            if(a.digital_read(9) == 1):

                print("je lance le des Mode button !!!!")
                value = lance_des()

                return value

        if(game._mode == "lumiere"):

            if(a.digital_read(9) < 500):
                print("je lance le des Mode lumiere !!!!")
                value = lance_des()

                return value

        if(game._mode == "temperature"):

            val = a.analog_read(2)
            temp = thermistor(val)

            if(temp > -40.57):
                print("je lance le des Mode lumiere !!!!")
                value = lance_des()

                return value


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

    time.sleep(1)
            
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.

    stop = 0
    while client.loop() == 0:

        
        if game._status == "wait" :
            client.publish("test/testdevice", "wait",0,False)
        if game._status == "playing" : 
            client.publish("test/testdevice", "playing",0,False)


        time.sleep(1)# sleep for 1 second before next call
    print ('CLOSING...')
    a.close()                     
