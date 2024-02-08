from kaooa_package.game import Game
from kaooa_package.definitions import *
from kaooa_package.functions import *

def main():
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                coord = get_near(x, y)
                if coord:
                    if game.turn == 0:
                        if game.crows_left > 0:
                            game.place_piece(coord)
                        elif not game.board.selected_piece and game.turn == 0:
                            piece = next((p for p in game.board.pieces if p.position == coord), None)
                            if piece and piece.piece_type == 0:
                                adjacent_positions = game.board.get_adjacent_positions(piece.position)
                                occupied = 0
                                for position in adjacent_positions:
                                    if game.is_occupied(position):
                                        occupied += 1
                                print(adjacent_positions, occupied)
                                if len(adjacent_positions) - occupied > 0:
                                    game.board.selected_piece = piece
                                else:
                                    game.board.selected_piece = None
                        else:
                            if game.move_piece(game.board.selected_piece, coord):
                                game.board.selected_piece = None
                    else:
                        if not game.vulture_placed:
                            game.place_piece(coord)
                        else:
                            vulture = next((p for p in game.board.pieces if p.piece_type == 1), None)
                            game.move_piece(vulture, coord)
                
        screen.blit(board_image, (0,0))
        for i in PLACE_HOLDERS:
            if game.crows_left > 0 and game.turn == 0 or not game.vulture_placed:
                pygame.draw.circle(screen, (0, 255, 0), i, 25, 5)
            else:
                pygame.draw.circle(screen, (255, 255, 255), i, 25, 5)
        if game.turn == 0:
            screen.blit(crow_text_base, (8, 15))
            screen.blit(crow_text, (10, 10))
            if not game.board.selected_piece and game.crows_left==0:
                # highlight all crows
                for piece in game.board.pieces:
                    if piece.piece_type == 0:
                        pygame.draw.circle(screen, (143, 0, 255), piece.position, 47, 7)
        else:
            screen.blit(vulture_text_base, (8, 15))
            screen.blit(vulture_text, (10, 10))
            vulture = next((p for p in game.board.pieces if p.piece_type == 1), None)
            if vulture:
                pygame.draw.circle(screen, (0, 255, 0), vulture.position, 50, 5)
        for piece in game.board.pieces:
            img = crow_image if piece.piece_type == 0 else vulture_image
            blit_image(img, *piece.position)
        if game.board.selected_piece:
            # highlighting the selected piece
            pygame.draw.circle(screen, (0, 255, 0), game.board.selected_piece.position, 47, 5)
        win_condition = game.update_game()
        if win_condition != -1:
            screen.fill((0, 0, 0))
            if win_condition == 0:
                blit_image(crow_image, 120, HEIGHT//2 + 25)
                screen.blit(crow_win, (175, HEIGHT//2))
            else:
                blit_image(vulture_image, 120, HEIGHT//2 + 25)
                screen.blit(vulture_win, (175, HEIGHT//2))

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
