from random import *

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[False for col in range(cols)] for row in range(rows)]

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_cell(self, row, col):
        if row < 0 or row >= self.get_rows() or col < 0 or col >= self.get_cols():
            return False
        return self.board[row][col]

    def set_cell(self, row, col, state):
        self.board[row][col] = state

    def get_neighbours(self, row, col):
        return [(row - 1, col - 1), (row - 1, col), (row -1, col+1), (row, col-1), (row,col+1), (row+1, col-1), (row+1, col),(row+1, col+1)]

    def get_neighbour_vals(self, row, col):
        return [self.get_cell(row1, col1) for (row1, col1) in self.get_neighbours(row, col)]

    def get_num_neigh(self, row, col):
        result = False
        for val in self.get_neighbour_vals(row, col):
            if val:
                result += 1
        return result

    def get_next_state(self, row, col):
        if self.get_cell(row, col):
            return self.get_num_neigh(row, col) == 2 or self.get_num_neigh(row, col) == 3
        else:
            return self.get_num_neigh(row, col) == 3

    def get_board_coords(self):
        return [(row, col) for row in range(self.get_rows()) for col in range(self.get_cols())]

    def get_next_board(self):
        nextBoard = Board(self.get_rows(), self.get_cols())
        for (row, col) in self.get_board_coords():
            nextBoard.set_cell(row, col, self.get_next_state(row, col))
        return nextBoard

    def get_number_filled(self):
        result = False
        for (row,col) in self.get_board_coords():
            if self.get_cell(row,col):
                result += 1
        return result

    def fill(self):
        for row in range(self.get_rows()):
            for col in range(self.get_cols()):
                val = False
                if randint(0,1) == 1:
                    val = True
                self.set_cell(row, col, val)