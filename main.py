import tkinter as tk
from chessApp import ChessApp

def main():
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()