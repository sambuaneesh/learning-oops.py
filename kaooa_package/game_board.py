from kaooa_package.definitions import *


class GameBoard:
    def __init__(self):
        self.pieces = []
        self.adjacent_positions = {
            PLACE_HOLDERS[0]: [PLACE_HOLDERS[2], PLACE_HOLDERS[3]],
            PLACE_HOLDERS[1]: [PLACE_HOLDERS[2], PLACE_HOLDERS[5]],
            PLACE_HOLDERS[2]: [
                PLACE_HOLDERS[0],
                PLACE_HOLDERS[1],
                PLACE_HOLDERS[3],
                PLACE_HOLDERS[5],
            ],
            PLACE_HOLDERS[3]: [
                PLACE_HOLDERS[0],
                PLACE_HOLDERS[2],
                PLACE_HOLDERS[4],
                PLACE_HOLDERS[6],
            ],
            PLACE_HOLDERS[4]: [PLACE_HOLDERS[3], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[5]: [
                PLACE_HOLDERS[1],
                PLACE_HOLDERS[2],
                PLACE_HOLDERS[7],
                PLACE_HOLDERS[8],
            ],
            PLACE_HOLDERS[6]: [
                PLACE_HOLDERS[3],
                PLACE_HOLDERS[4],
                PLACE_HOLDERS[7],
                PLACE_HOLDERS[9],
            ],
            PLACE_HOLDERS[7]: [
                PLACE_HOLDERS[5],
                PLACE_HOLDERS[6],
                PLACE_HOLDERS[8],
                PLACE_HOLDERS[9],
            ],
            PLACE_HOLDERS[8]: [PLACE_HOLDERS[5], PLACE_HOLDERS[7]],
            PLACE_HOLDERS[9]: [PLACE_HOLDERS[6], PLACE_HOLDERS[7]],
        }
        self.jumping_positions = {
            PLACE_HOLDERS[0]: [PLACE_HOLDERS[5], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[1]: [PLACE_HOLDERS[3], PLACE_HOLDERS[7]],
            PLACE_HOLDERS[2]: [PLACE_HOLDERS[4], PLACE_HOLDERS[8]],
            PLACE_HOLDERS[3]: [PLACE_HOLDERS[1], PLACE_HOLDERS[9]],
            PLACE_HOLDERS[4]: [PLACE_HOLDERS[2], PLACE_HOLDERS[7]],
            PLACE_HOLDERS[5]: [PLACE_HOLDERS[0], PLACE_HOLDERS[9]],
            PLACE_HOLDERS[6]: [PLACE_HOLDERS[8], PLACE_HOLDERS[0]],
            PLACE_HOLDERS[7]: [PLACE_HOLDERS[1], PLACE_HOLDERS[4]],
            PLACE_HOLDERS[8]: [PLACE_HOLDERS[2], PLACE_HOLDERS[6]],
            PLACE_HOLDERS[9]: [PLACE_HOLDERS[3], PLACE_HOLDERS[5]],
        }
        self.selected_piece = None
        self.occupied_positions = []

    def get_adjacent_positions(self, position):
        return self.adjacent_positions[position]

    def is_jump_valid(self, pos1, pos2):
        return pos2 in self.jumping_positions[pos1]

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def is_move_valid(self, piece, new_position):
        global captured_crows
        if new_position not in PLACE_HOLDERS:
            return False

        if new_position in [p.position for p in self.pieces]:
            return False

        if piece.piece_type == 0:
            return new_position in self.get_adjacent_positions(piece.position)

        elif piece.piece_type == 1:
            if new_position in self.get_adjacent_positions(piece.position):
                return True
            else:
                if self.is_jump_valid(piece.position, new_position):
                    adj1 = self.get_adjacent_positions(piece.position)
                    adj2 = self.get_adjacent_positions(new_position)
                    for p in self.pieces:
                        if (
                            p.position in adj1
                            and p.position in adj2
                            and p.piece_type == 0
                        ):
                            self.pieces.remove(p)
                            captured_crows += 1
                            return True
                    return False
            return False

    def is_vulture_trapped(self):
        vulture_piece = next((p for p in self.pieces if p.piece_type == 1), None)
        if not vulture_piece:
            return False
        available_positions = []
        adjacent_positions = self.get_adjacent_positions(vulture_piece.position)
        jump_positions = self.jumping_positions[vulture_piece.position]
        available_positions.extend(adjacent_positions)
        available_positions.extend(jump_positions)
        for pos in available_positions:
            if pos not in [p.position for p in self.pieces]:
                return False  # Vulture has at least one valid move
        return True  # No valid moves found

    def is_win_condition_met(self):
        if captured_crows >= 4:
            return 1
        if self.is_vulture_trapped():
            return 0
        return -1
