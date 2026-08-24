from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        #Create ten separate PlayerList objects for collection handling
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

        #Track the total number of players stored in the hashmap.
        self.__size = 0

    def get_index(self, key: str | Player) -> int:
        #Use the players magic hash method when given a player object
        if isinstance(key, Player):
            player_hash = hash(key)
        else:
            #Hash a string UID using the player class's hash method
            player_hash = Player.hash(key)

        #Convert the hash into a valid index from 0 to 9
        return player_hash % self.SIZE

