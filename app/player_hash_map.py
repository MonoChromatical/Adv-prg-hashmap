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

    def __setitem__(self, key: str, name: str) -> None:
        # Find the PlayerList where this player belongs.
        index = self.get_index(key)
        player_list = self.hashmap[index]

        # Check whether the player is already in that list.
        existing_node = player_list.find_by_key(key)

        if existing_node is not None:
            # Update the existing player's name without adding a duplicate.
            existing_node.player.player_name = name
            return

        # Create a new player and wrap it inside a linked-list node.
        new_player = Player(key, name)
        new_node = PlayerNode(new_player)

        # Add the node to the selected collision list.
        player_list.insert_at_tail(new_node)

        # Count the newly added player.
        self.__size += 1

    def __getitem__(self, key: str) -> Player:
        #Find the PlayerList where the player should be stored
        index = self.get_index(key)
        player_list = self.hashmap[index]

        #search the selected list for the requested key
        player_node = player_list.find_by_key(key)

        #Raise an error when the player does not exist
        if player_node is None:
            raise KeyError(key)

        #Return the Player rather than its linked_list node.
        return player_node.player

    def __delitem__(self, key: str) -> None:
        # Find the PlayerList where the player should be stored.
        index = self.get_index(key)
        player_list = self.hashmap[index]

        # Attempt to remove the player from that list.
        removed_node = player_list.delete_by_key(key)

        # Raise an error when the player does not exist.
        if removed_node is None:
            raise KeyError(key)

        # Update the number of players in the hashmap.
        self.__size -= 1

    def __len__(self) -> int:
        #Return the number of players stored in the hashmaps
        return self.__size

    def display(self) -> None:
        #Visit every bucket and keep track of its index
        for index, player_list in enumerate(self.hashmap):
            #only display PlayerLists that contain players.
            if not player_list.is_empty:
                print(f"Index {index}:")

                #start at the head of the collision list
                current_node = player_list.head

                #print every player stored in this bucket
                while current_node is not None:
                    print(current_node.player)
                    current_node = current_node.next
