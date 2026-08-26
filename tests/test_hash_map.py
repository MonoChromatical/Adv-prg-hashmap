import unittest
from unittest.mock import patch

from app.player import Player
from app.player_hash_map import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        # Create a new empty hashmap before every test.
        self.player_hash_map = PlayerHashMap()

    def find_collision_keys(self):
        # Store the first player key found for each hashmap index.
        keys_by_index = {}

        for number in range(100):
            key = f"P{number:03}"
            index = self.player_hash_map.get_index(key)

            # A reused index means that the two keys collide.
            if index in keys_by_index:
                return keys_by_index[index], key

            keys_by_index[index] = key

        self.fail("No collision was found")

    def test_hashmap_starts_empty(self):
        # A new hashmap should contain no players.
        self.assertEqual(len(self.player_hash_map), 0)

        # The hashmap should contain ten PlayerList buckets.
        self.assertEqual(len(self.player_hash_map.hashmap), 10)

    def test_add_player(self):
        # Add a player using dictionary syntax.
        self.player_hash_map["P001"] = "Alex"

        # The hashmap should now contain one player.
        self.assertEqual(len(self.player_hash_map), 1)

    def test_get_player(self):
        # Add and retrieve a player.
        self.player_hash_map["P001"] = "Alex"
        player = self.player_hash_map["P001"]

        # Check that the correct Player was returned.
        self.assertIsInstance(player, Player)
        self.assertEqual(player.uid, "P001")
        self.assertEqual(player.player_name, "Alex")

    def test_update_player_name(self):
        # Add a player and then update the same UID.
        self.player_hash_map["P001"] = "Alex"
        self.player_hash_map["P001"] = "Alexander"

        # The name should change without adding another player.
        player = self.player_hash_map["P001"]

        self.assertEqual(player.player_name, "Alexander")
        self.assertEqual(len(self.player_hash_map), 1)

    def test_remove_player(self):
        # Add and then remove a player.
        self.player_hash_map["P001"] = "Alex"
        del self.player_hash_map["P001"]

        # The hashmap should be empty again.
        self.assertEqual(len(self.player_hash_map), 0)

    def test_get_missing_player_raises_key_error(self):
        # Retrieving an unknown UID should raise KeyError.
        with self.assertRaises(KeyError):
            self.player_hash_map["P999"]

    def test_remove_missing_player_raises_key_error(self):
        # Removing an unknown UID should raise KeyError.
        with self.assertRaises(KeyError):
            del self.player_hash_map["P999"]

    def test_collision_handling(self):
        # Find two different keys that produce the same hashmap index.
        first_key, second_key = self.find_collision_keys()

        # Confirm that the keys use the same bucket.
        self.assertEqual(
            self.player_hash_map.get_index(first_key),
            self.player_hash_map.get_index(second_key),
        )

        # Add both players to the collision list.
        self.player_hash_map[first_key] = "Alex"
        self.player_hash_map[second_key] = "Sam"

        # Both players should still be retrievable.
        self.assertEqual(
            self.player_hash_map[first_key].player_name,
            "Alex",
        )
        self.assertEqual(
            self.player_hash_map[second_key].player_name,
            "Sam",
        )
        self.assertEqual(len(self.player_hash_map), 2)

    def test_remove_one_colliding_player(self):
        # Find and add two players that use the same bucket.
        first_key, second_key = self.find_collision_keys()
        self.player_hash_map[first_key] = "Alex"
        self.player_hash_map[second_key] = "Sam"

        # Remove only the first player.
        del self.player_hash_map[first_key]

        # The other player should remain accessible.
        self.assertEqual(
            self.player_hash_map[second_key].player_name,
            "Sam",
        )
        self.assertEqual(len(self.player_hash_map), 1)

    def test_display(self):
        # Add a player before calling display.
        self.player_hash_map["P001"] = "Alex"
        expected_index = self.player_hash_map.get_index("P001")

        # Temporarily monitor calls made to print().
        with patch("builtins.print") as mock_print:
            self.player_hash_map.display()

        # Check that the index and player were printed.
        mock_print.assert_any_call(f"Index {expected_index}:")
        mock_print.assert_any_call(self.player_hash_map["P001"])


if __name__ == "__main__":
    unittest.main()