import unittest
from Game import Game as g


class TestGame(unittest.TestCase):
    def test_player_win(self):
        computer_handsign = "rock"
        player_handsign = "paper"
        self.assertEqual(201, g.compare(self, computer_handsign, player_handsign))

    def test_player_lose(self):
        player_handsign = "rock"
        computer_handsign = "paper"
        self.assertEqual(204, g.compare(self, computer_handsign, player_handsign))

    def test_drow(self):
        player_handsign = "rock"
        computer_handsign = "rock"
        self.assertEqual(418, g.compare(self, computer_handsign, player_handsign))

    def test_wrong_input(self):
        player_handsign = "other"
        self.assertEqual(400, g.check(self, player_handsign))


if __name__ == '__main__':
    unittest.main()