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

    def __str__(self):
        return f"player ID: {self.__unique_id}, player name: {self.__player_name}"