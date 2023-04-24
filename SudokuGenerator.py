import random

class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells
        self.board = []

    def get_board(self):
        self.board = [[0 for i in range(self.row_length)] for j in range(9)]
        return self.board

    def print_board(self):
        print(self.board)

    def valid_in_row(self, row, num):
        for i in range(9):
            if self.board[row][i] == num:
                return True
        return False

    def valid_in_col(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return True
        return False

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + i] == num:
                    return True
        return False

    def is_valid(self, row, col, num):
        if self.board[row][col] == num:
            return True
        return False
