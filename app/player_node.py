from app.player import Player

class PlayerNode:
    def __init__(self, player: Player):
        self.__player = player
        self.__next = None
        self.__previous = None


    @property
    def player(self):
        return self.__player

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, node):
        self.__previous = node


    @property
    def key(self):
        return self.__player.uid

    def __str__(self):
        return f"PlayerNode: {self.__player}"