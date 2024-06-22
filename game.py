import tkinter as tk
from tkinter import messagebox
from board import Board
from player import Player
from ai import AI
from king import King


class Game:
    def __init__(self, root, against_ai):
        self.root = root
        self.against_ai = against_ai
        self.board = Board()
        self.players = [Player('white'), AI('black')] if against_ai else [Player('white'), Player('black')]
        self.current_player_index = 0
        self.move_history = []
        self.selected_piece = None

    def start_game(self):
        self.setup_board_ui()

    def setup_board_ui(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        for x in range(8):
            for y in range(8):
                frame = tk.Frame(self.board_frame, width=60, height=60)
                frame.grid(row=y, column=x)
                color = 'white' if (x + y) % 2 == 0 else 'gray'
                canvas = tk.Canvas(frame, width=60, height=60, bg=color)
                canvas.bind("<Button-1>", lambda event, x=x, y=y: self.on_square_click(x, y))
                canvas.pack()
                self.squares[x][y] = canvas

        self.update_board_ui()

    def on_square_click(self, x, y):
        print(f'Square clicked: {x}, {y}')
        square = self.board.squares[x][y]
        if self.selected_piece:
            if square in self.selected_piece.get_valid_moves(self.board):
                self.move_piece(self.selected_piece, square)
            self.selected_piece = None
        elif square.is_occupied() and square.get_piece().color == self.current_player().color:
            self.selected_piece = square.get_piece()

        self.update_board_ui()

    def move_piece(self, piece, to_square):
        from_square = piece.position
        from_square.piece = None
        to_square.piece = piece
        piece.position = to_square
        piece.has_moved = True
        self.move_history.append((piece, from_square, to_square))
        self.current_player_index = 1 - self.current_player_index

        if self.is_in_check(self.current_player().color):
            if self.is_checkmate(self.current_player().color):
                messagebox.showinfo("Fim de Jogo", f"Xeque-mate! {self.current_player().color} perdeu.")
            else:
                messagebox.showinfo("Aviso", f"Xeque ao rei {self.current_player().color}!")

    def update_board_ui(self):
        for x in range(8):
            for y in range(8):
                self.squares[x][y].delete("all")
                piece = self.board.squares[x][y].get_piece()
                if piece:
                    self.squares[x][y].create_text(30, 30, text=piece.symbol, font=("Arial", 24))

    def current_player(self):
        return self.players[self.current_player_index]

    def is_in_check(self, color):
        king_square = None
        for row in self.board.squares:
            for square in row:
                piece = square.get_piece()
                if isinstance(piece, King) and piece.color == color:
                    king_square = square
                    break
            if king_square:
                break
        if not king_square:
            return False

        for row in self.board.squares:
            for square in row:
                piece = square.get_piece()
                if piece and piece.color != color:
                    if king_square in piece.get_valid_moves(self.board):
                        return True
        return False

    def is_checkmate(self, color):
        for row in self.board.squares:
            for square in row:
                piece = square.get_piece()
                if piece and piece.color == color:
                    valid_moves = piece.get_valid_moves(self.board)
                    for move in valid_moves:
                        original_square = piece.position
                        target_piece = move.get_piece()
                        original_square.piece = None
                        move.piece = piece
                        piece.position = move
                        if not self.is_in_check(color):
                            move.piece = target_piece
                            original_square.piece = piece
                            piece.position = original_square
                            return False
                        move.piece = target_piece
                        original_square.piece = piece
                        piece.position = original_square
        return True