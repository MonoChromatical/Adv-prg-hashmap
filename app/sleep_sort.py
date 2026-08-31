import threading
import time

from app.player import Player


def sleep_sort(players: list[Player]) -> list[Player]:
    # Return an empty list if there are no players.
    if not players:
        return []

    # Find the highest score.
    max_score = max(player.score for player in players)

    # Maximum amount of time a player can wait.
    wait_time = 1

    # Store players in the order they wake up.
    sorted_players = []

    # Prevent multiple threads from modifying the list at once.
    lock = threading.Lock()

    def wait_and_add(player: Player):
        # A score of zero should be added immediately.
        if max_score == 0:
            delay = 0
        else:
            # Calculate the delay based on the player's score.
            delay = (player.score / max_score) * wait_time

        # Wait for the calculated amount of time.
        time.sleep(delay)

        # Add the player to the result.
        with lock:
            sorted_players.append(player)

    # Create a thread for each player.
    threads = []

    for player in players:
        thread = threading.Thread(
            target=wait_and_add,
            args=(player,)
        )

        threads.append(thread)
        thread.start()

    # Wait for all threads to finish.
    for thread in threads:
        thread.join()

    return sorted_players