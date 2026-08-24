import random


# Create the same shuffled lookup table each time the program runs.
random.seed(42)
pearson_table = list(range(256))
random.shuffle(pearson_table)


class Player:
    def __init__(self, unique_id: str, player_name: str):
        self.__unique_id = unique_id
        self.__player_name = player_name


    @property
    def uid(self):
        return self.__unique_id


    @property
    def player_name(self):
        return self.__player_name


    @player_name.setter
    def player_name(self, new_name):
        self.__player_name = new_name


    @classmethod
    def hash(cls, key: str) -> int:
        # Start the Pearson hash value at zero.
        hash_value = 0

        # Use the lookup table to process each character in the key.
        for character in key:
            hash_value = pearson_table[hash_value ^ ord(character)]

        return hash_value


    def __hash__(self) -> int:
        return self.hash(self.uid)


    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.uid == other.uid


    def __str__(self):
        return f"player ID: {self.__unique_id}, player name: {self.__player_name}"