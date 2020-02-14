import unittest
from game_of_life import Board

class GameOfLifeTests(unittest.TestCase):

    def testRows(self):
        board = Board(3,4)
        self.assertEqual(board.get_rows(), 3)
        self.assertEqual(board.get_cols(), 4)


if __name__ == "__main__":
    unittest.main() # run all tests