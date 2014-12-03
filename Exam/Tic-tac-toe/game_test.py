import unittest

from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_constructor(self):
        self.assertEqual(self.game._board, [[0, 0, 0],
                                            [0, 0 ,0],
                                            [0, 0, 0]])
