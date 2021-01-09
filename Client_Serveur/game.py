class game:
    def __init__(self):
        self._players = []
        self._nbPlayerNeeded = 0
        self._status = "wait" # wait for players



    def setPlayer(self , player):
        self._players.append(player)


    def setStatus(self, status):
        self._status = status

    def getRes(self) :
        res = 0
        for player in self._players :
            res += player.get('res')
        return res
    

    