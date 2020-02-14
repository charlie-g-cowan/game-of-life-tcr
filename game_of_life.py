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