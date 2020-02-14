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

    def testNeighbours(self):
        board = Board(3, 4)
        self.assertEqual(board.get_neighbours(3, 4), [(2, 3), (2, 4), (2, 5), (3, 3), (3, 5), (4, 3), (4, 4), (4, 5)])

    def testNeighbourVals(self):
        board = Board(4, 5)
        self.assertEqual(board.get_neighbour_vals(3,4), [False, False, False, False, False, False, False, False])

if __name__ == "__main__":
    unittest.main() # run all tests