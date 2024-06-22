class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None

    def is_occupied(self):
        return self.piece is not None

    def get_piece(self):
        return self.piece
