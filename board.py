from cell import Cell

class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            row_values = [cell.value if cell.value else "-" for cell in row]
            print(" | ".join(row_values))
        print()

    def make_move(self, row, col, symbol):
        if 0 <= row < self.size and 0 <= col < self.size:
            if self.grid[row][col].is_empty():
                self.grid[row][col].value = symbol
                return True
        return False

    def check_winner(self, symbol):
        for i in range(self.size):
            if all(self.grid[i][j].value == symbol for j in range(self.size)) or \
               all(self.grid[j][i].value == symbol for j in range(self.size)):
                return True

        if all(self.grid[i][i].value == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1].value == symbol for i in range(self.size)):
            return True

        return False

    def is_full(self):
        return all(not cell.is_empty() for row in self.grid for cell in row)
