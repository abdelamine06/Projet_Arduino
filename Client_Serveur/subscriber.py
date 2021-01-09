import paho.mqtt.client as mqtt
import json
import time
import random
import game
import player

begin = True
game = game.game()
players = []
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global begin
    while begin == True:
        print("************** Lancement du jeu ***************")
        begin = False
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/testdevice")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = msg.payload
    data = data.decode("utf-8")

    # Add particpant while nbr player <4
    if(len(game._players) <  4):
        info = data.split(':')
        if(len(info) == 2):
            if(game._status == "wait"):
                print("Attendre...")
                if((info[0] not in players)):
                    players.append(info[0])
                    info[0] = player.player(info[0], int(info[1]))
                    game.setPlayer(info[0])

    # Test if all players are here
    elif(len(game._players) == 4):
        game.setStatus("start")
        info = data.split(':')
        if(len(info) == 2):
            for ply in game._players:
                if ply._player == info[0]:

                    if ply._status == "playing":
                        pass 

                    elif int(info[1]) != 0:
                        ply.setScore(int(info[1]))
                        ply.setStatus("playing")
                        print(info[0]+" Viens de jouer, il a eu : "+info[1])
                        game._nbPlayerNeeded+=1
                
                    elif ply._status == "wait":
                        print(info[0]+" N'a pas encore jouer "+ ply._score)
    

    #Test if party is done
    if(game._nbPlayerNeeded == 2): 
        game.setStatus("finish")
        game._nbPlayerNeeded = 0
        max = 0
        i=0
        f=0
        print("************** Fin ***************") 
        time.sleep(2)

        for ply in game._players:
            if ( ply._score > max):
                max =  ply._score
                f=i
            i+=1    
        print("Le gagnant est : " +(game._players[f])._player + " avec un score de " + str((game._players[f])._score))
    
    global begin
    while begin == False:
        time.sleep(5)
        print("Qui va jouer?")
        begin = True
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org")
client.loop_forever()
