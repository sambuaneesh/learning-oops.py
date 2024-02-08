from kaooa_package.game_board import GameBoard
from kaooa_package.game_piece import GamePiece
from kaooa_package.definitions import *


class Game:
    def __init__(self):
        self.board = GameBoard()
        self.turn = 0  # 0 = crows 1 = vulture
        self.crows_left = 7
        self.vulture_placed = False

    def is_occupied(self, position):
        return position in [p.position for p in self.board.pieces]

    def place_piece(self, position):
        if self.is_occupied(position):
            return
        if self.turn == 0 and self.crows_left > 0:
            self.board.add_piece(GamePiece(0, position))
            self.crows_left -= 1
        elif self.turn == 1 and not self.vulture_placed:
            self.board.add_piece(GamePiece(1, position))
            self.vulture_placed = True
        self.turn ^= 1

    def move_piece(self, piece, new_position):
        if self.turn == 1 and self.board.is_move_valid(piece, new_position):
            if piece.piece_type == 1:
                piece.move(new_position)
                self.turn ^= 1
                self.update_game()
                return True
        elif self.board.is_move_valid(piece, new_position):
            if piece.piece_type == 0:
                piece.move(new_position)
                self.turn ^= 1
                self.update_game()
                return True
        return False

    def update_game(self):
        win_condition = self.board.is_win_condition_met()
        return win_condition
