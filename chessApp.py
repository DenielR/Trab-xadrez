import tkinter as tk
from tkinter import messagebox
from game import Game

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Xadrez")
        self.main_menu()

    def main_menu(self):
        self.clear_screen()
        
        label = tk.Label(self.root, text="Bem-vindo ao Jogo de Xadrez!", font=("Arial", 24))
        label.pack(pady=20)
        
        play_player_btn = tk.Button(self.root, text="Jogar contra Jogador", command=self.start_game_vs_player, font=("Arial", 18))
        play_player_btn.pack(pady=10)
        
        play_ai_btn = tk.Button(self.root, text="Jogar contra a Máquina", command=self.start_game_vs_ai, font=("Arial", 18))
        play_ai_btn.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_game_vs_player(self):
        self.clear_screen()
        game = Game(self.root, against_ai=False)
        game.start_game()

    def start_game_vs_ai(self):
        self.clear_screen()
        game = Game(self.root, against_ai=True)
        game.start_game()