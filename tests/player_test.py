import unittest

from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList
from app.sleep_sort import sleep_sort


class TestPlayer(unittest.TestCase):

    def test_uid_returns_player_id(self):
        player = Player("P001", "Alex")

        self.assertEqual(player.uid, "P001")

    def test_name_returns_player_name(self):
        player = Player("P001", "Alex")

        self.assertEqual(player.player_name, "Alex")

    def test_insert_at_head_when_list_is_empty(self):
        node = PlayerNode(Player("P001", "Alex"))
        player_list = PlayerList()

        player_list.insert_at_head(node)

        self.assertFalse(player_list.is_empty)
        self.assertIs(player_list.head, node)
        self.assertIs(player_list.tail, node)
        self.assertIsNone(node.previous)
        self.assertIsNone(node.next)

    def test_insert_at_head_when_list_is_not_empty(self):
        first_node = PlayerNode(Player("P001", "Alex"))
        second_node = PlayerNode(Player("P002", "Sam"))
        player_list = PlayerList()

        player_list.insert_at_head(first_node)
        player_list.insert_at_head(second_node)

        self.assertIs(player_list.head, second_node)
        self.assertIs(player_list.tail, first_node)
        self.assertIs(second_node.next, first_node)
        self.assertIs(first_node.previous, second_node)
        self.assertIsNone(second_node.previous)
        self.assertIsNone(first_node.next)

    def test_insert_at_tail(self):
        first_node = PlayerNode(Player("P001", "Alex"))
        second_node = PlayerNode(Player("P002", "Sam"))
        player_list = PlayerList()

        player_list.insert_at_tail(first_node)
        player_list.insert_at_tail(second_node)

        self.assertIs(player_list.head, first_node)
        self.assertIs(player_list.tail, second_node)
        self.assertIs(first_node.next, second_node)
        self.assertIs(second_node.previous, first_node)
        self.assertIsNone(first_node.previous)
        self.assertIsNone(second_node.next)

    def test_delete_at_head(self):
        first_node = PlayerNode(Player("P001", "Alex"))
        second_node = PlayerNode(Player("P002", "Sam"))
        player_list = PlayerList()

        player_list.insert_at_tail(first_node)
        player_list.insert_at_tail(second_node)

        removed_node = player_list.delete_at_head()

        self.assertIs(removed_node, first_node)
        self.assertIs(player_list.head, second_node)
        self.assertIs(player_list.tail, second_node)
        self.assertIsNone(second_node.previous)
        self.assertIsNone(removed_node.next)

    def test_delete_at_tail(self):
        first_node = PlayerNode(Player("P001", "Alex"))
        second_node = PlayerNode(Player("P002", "Sam"))
        player_list = PlayerList()

        player_list.insert_at_tail(first_node)
        player_list.insert_at_tail(second_node)

        removed_node = player_list.delete_at_tail()

        self.assertIs(removed_node, second_node)
        self.assertIs(player_list.head, first_node)
        self.assertIs(player_list.tail, first_node)
        self.assertIsNone(first_node.next)
        self.assertIsNone(removed_node.previous)

    def test_delete_by_key(self):
        first_node = PlayerNode(Player("P001", "Alex"))
        middle_node = PlayerNode(Player("P002", "Sam"))
        last_node = PlayerNode(Player("P003", "Jordan"))
        player_list = PlayerList()

        player_list.insert_at_tail(first_node)
        player_list.insert_at_tail(middle_node)
        player_list.insert_at_tail(last_node)

        removed_node = player_list.delete_by_key("P002")

        self.assertIs(removed_node, middle_node)
        self.assertIs(first_node.next, last_node)
        self.assertIs(last_node.previous, first_node)
        self.assertIsNone(removed_node.previous)
        self.assertIsNone(removed_node.next)

    def test_sort_players(self):
        players = [
            Player("01", "Alice", score=10),
            Player("02", "Bob", score=5),
            Player("03", "Charlie", score=15)
        ]

        sorted_players = sorted(players)

        manually_sorted_players = [
            Player("02", "Bob", score=5),
            Player("01", "Alice", score=10),
            Player("03", "Charlie", score=15)
        ]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        alice = Player("01", "Alice", score=10)
        bob = Player("02", "Bob", score=5)

        self.assertGreater(alice, bob)

    def test_sleep_sort_players(self):
        players = [
            Player("01", "Alice", score=10),
            Player("02", "Bob", score=5),
            Player("03", "Charlie", score=15)
        ]

        sorted_players = sleep_sort(players)

        self.assertEqual(sorted_players[0].player_name, "Bob")
        self.assertEqual(sorted_players[1].player_name, "Alice")
        self.assertEqual(sorted_players[2].player_name, "Charlie")

    def test_sleep_sort_empty_list(self):
        players = []

        sorted_players = sleep_sort(players)

        self.assertEqual(sorted_players, [])

    def test_sleep_sort_single_player(self):
        players = [
            Player("01", "Alice", score=10)
        ]

        sorted_players = sleep_sort(players)

        self.assertEqual(sorted_players, players)



if __name__ == '__main__':
    unittest.main()