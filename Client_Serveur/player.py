class player:
    def __init__(self, id):
        self._id = id
        self._players = {}
        self._nbPlayerNeeded = 4
        self._resMini = 12
        self._status = "wait" # wait for players
        self._mode = "button"