import tkinter as tk
import random


class TicTacToe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Tic Tac Toe")
        self.grid()
        self.create_widgets()
        self.player = "X"
        self.computer = "O"

    def create_widgets(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self,
                    text="",
                    width=5,
                    height=2,
                    font=("Helvetica", 20),
                    command=lambda row=i, col=j: self.on_click(row, col),
                )
                button.grid(row=i, column=j)
                self.board[i][j] = button
        self.reset_button = tk.Button(
            self, text="Reset", font=("Helvetica", 16), command=self.reset_game
        )
        self.reset_button.grid(row=3, column=1)

    def on_click(self, row, col):
        button = self.board[row][col]
        if button["text"] != "":
            return
        button["text"] = self.player
        if self.check_win(self.player):
            self.disable_board()
            tk.messagebox.showinfo("Tic Tac Toe", "You win!")
        elif self.check_tie():
            self.disable_board()
            tk.messagebox.showinfo("Tic Tac Toe", "Game over. It's a tie!")
        else:
            self.player = self.computer
            self.computer_move()

    def check_win(self, player):
        for i in range(3):
            if (
                self.board[i][0]["text"]
                == self.board[i][1]["text"]
                == self.board[i][2]["text"]
                == player
            ):
                return True
        for j in range(3):
            if (
                self.board[0][j]["text"]
                == self.board[1][j]["text"]
                == self.board[2][j]["text"]
                == player
            ):
                return True
        if (
            self.board[0][0]["text"]
            == self.board[1][1]["text"]
            == self.board[2][2]["text"]
            == player
        ):
            return True
        if (
            self.board[0][2]["text"]
            == self.board[1][1]["text"]
            == self.board[2][0]["text"]
            == player
        ):
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]["text"] == "":
                    return False
        return True

    def computer_move(self):
        # First, check if the computer can win in the next move
        for i in range(3):
            for j in range(3):
                if self.board[i][j]["text"] == "":
                    self.board[i][j]["text"] = self.computer
                    if self.check_win(self.computer):
                        self.disable_board()
                        tk.messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                        return
                    self.board[i][j]["text"] = ""

        # Next, check if the player can win in the next move and block them
        for i in range(3):
            for j in range(3):
                if self.board[i][j]["text"] == "":
                    self.board[i][j]["text"] = self.player
                    if self.check_win(self.player):
                        self.board[i][j]["text"] = self.computer
                        self.player = "X"
                        return
                    self.board[i][j]["text"] = ""

        # If neither the player nor the computer can win in the next move, make a random move
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row][col]["text"] == "":
                self.board[row][col]["text"] = self.computer
                self.player = "X"
                break

        # Check for win or tie conditions
        if self.check_win(self.computer):
            self.disable_board()
            tk.messagebox.showinfo("Tic Tac Toe", "Computer wins!")
        elif self.check_tie():
            self.disable_board()
            tk.messagebox.showinfo("Tic Tac Toe", "Game over. It's a tie!")

    def disable_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j].configure(state="disabled")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j]["text"] = ""
                self.board[i][j].configure(state="normal")
        self.player = "X"
        self.computer = "O"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    game.mainloop()
