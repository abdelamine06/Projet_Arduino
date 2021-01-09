import json

class player:

    def __init__(self,player, score):
        self._player = player
        self._score = score
        self._status = "wait" 

    def setPlayer(self , player):
        self._player = player
        # ne pas ajouter à gerer plus tard.


    def setScore(self, score):
        self._score = score

    def setStatus(self, status):
        self._status = status
    