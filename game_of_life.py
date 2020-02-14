class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[False for col in range(cols)] for row in range(rows)]

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols