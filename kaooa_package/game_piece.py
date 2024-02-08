class GamePiece:
    def __init__(self, piece_type, position):
        self.piece_type = piece_type
        self.position = position

    def move(self, new_position):
        self.position = new_position
