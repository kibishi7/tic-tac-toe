from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def start(self):
        while True:
            self.board.display()
            print(f"{self.current_player.name}'s Turn ({self.current_player.symbol})")

            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print(" Invalid input. Please enter numbers only.")
                continue

            if not self.board.make_move(row, col, self.current_player.symbol):
                print(" Invalid move! Cell is already taken or out of range.")
                continue

            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                print(f" {self.current_player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print(" It's a draw!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = Game()
    game.start()
