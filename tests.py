import unittest
from game_of_life import Board

class GameOfLifeTests(unittest.TestCase):

    def testRows(self):
        board = Board(3,4)
        self.assertEqual(board.get_rows(), 3)
        self.assertEqual(board.get_cols(), 4)

    def testGetCell(self):
        board = Board(3,4)
        self.assertEqual(board.get_cell(1,1), False)
        self.assertEqual(board.get_cell(-1,-1), False)
        self.assertEqual(board.get_cell(3,4), False)

    def testSetCell(self):
        board = Board(3, 4)
        self.assertEqual(board.get_cell(1, 1), False)
        board.set_cell(1, 1, True)
        self.assertEqual(board.get_cell(1, 1), True)
        self.assertEqual(board.get_cell(-1, -1), False)
        self.assertEqual(board.get_cell(3, 4), False)

if __name__ == "__main__":
    unittest.main() # run all tests