import json

class game:

    def __init__(self,player):
        self._players = {}
        self._player = player
        self._nbPlayerNeeded = 4
        self._resMini = 12
        self._status = "playing" # wait for players
    def setPlayer(self , player):
        if ( len(self._players) < self._nbPlayerNeeded) :
            self._players.update(player)
        # ne pas ajouter à gerer plus tard.

    def getLenght(self) :
        return len(self._players)

    def getRes(self) :
        res = 0
        for player in self._players :
            res += player.get('res')
        return res

    def asDict(self):
        return { 'id' : self._id , 'players' : self._players , 'nbPlayerNeeded' : self._nbPlayerNeeded, 'resMini' : self._resMini}
    

    