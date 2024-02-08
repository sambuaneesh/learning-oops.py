import pygame
import math
from time import sleep

graph = [
         [2, 3],
         [2, 5],
         [0, 1, 3, 5],
         [0, 2, 4, 6],
         [3, 6],
         [1, 2, 7, 8],
         [3, 4 ,7, 9],
         [5, 6, 8, 9],
         [5, 7],
         [6, 7]
         ]

jump = [
    [5, 6],
    [3, 7],
    [4, 8],
    [1, 9],
    [2, 7],
    [0, 9],
    [0, 8],
    [1, 4],
    [2, 6],
    [3, 5]
]


class Game:
    def __init__(self, SCREEN_WIDTH=600, SCREEN_HEIGHT=400):
        pygame.init()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.THRESHOLD = 15
        self.center = (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Kaooa")
        self.image = pygame.image.load("board.png")
        self.image_rect = self.image.get_rect()
        self.circle_radius = 20
        self.crow_color = (128, 128, 128) # grey
        self.vulture_color = (255, 255, 0) # yellow
        self.font = pygame.font.Font(None, 30) 
        self.crows = 7
        self.run = True
        self.cords = [(261, 25), (136, 196), (263, 156), (343, 130), (466, 88), (261, 243), (390, 197), (345, 265), (267, 375), (472, 304)]
        self.circles = []
        self.backup_circles = []
        self.turn = 0 # 0 -> crow, 1 -> vulture, -1 -> buffer
        self.vulture = None
        self.removed_circle = None
        self.kill = None
        self.vulture_score = 0
        self.winner = -1

    def process_board(self):
        self.screen.fill((255, 255, 255))
        self.image_x = (self.SCREEN_WIDTH - self.image_rect.width) // 2
        self.image_y = (self.SCREEN_HEIGHT - self.image_rect.height) // 2
        self.circle_x = self.SCREEN_WIDTH - self.circle_radius * 2 
        self.circle_y = self.SCREEN_HEIGHT - self.circle_radius * 2
        self.text = self.font.render(f"Crows Remaining: {self.crows}", True, (0, 0, 0)) 
        self.text_rect = self.text.get_rect()
        self.text_rect.topleft = (self.circle_x - self.text_rect.width, self.circle_y)
        self.screen.blit(self.image, (self.image_x, self.image_y))
        if (self.crows > 0) :
            self.screen.blit(self.text, self.text_rect)
            pygame.draw.circle(self.screen, self.crow_color, (self.circle_x, self.circle_y - 30), self.circle_radius)
        
        self.render_circles()

    def get_circle(self, pos):
        x, y = pos[0], pos[1]
        for centers in self.cords:
            dist = math.sqrt((centers[0] - x)**2 + (centers[1] - y)**2)
            if dist <= self.THRESHOLD: return centers
        
    def add_circle(self, pos):
        self.circles.append((pos[0], pos[1]))
    
    def render_circles(self):
        for circles in self.circles:
            x, y = circles
            pygame.draw.circle(self.screen, self.crow_color, (x, y), self.circle_radius)
            if self.vulture == circles:
                pygame.draw.circle(self.screen, self.vulture_color, (x, y), self.circle_radius)

    def adjacent(self, c1, c2):
        # checks if two circles are adjacent
        c1id = self.cords.index(c1)
        c2id = self.cords.index(c2)
        return c1id in graph[c2id]
    
    def check_win(self):
        if self.vulture is None: return False
        
        if self.vulture_score >= 4:
            self.winner = 1
            return True

        vulture_node = self.cords.index(self.vulture)
        res = True
        for node in graph[vulture_node]:
            if self.cords[node] not in self.circles: res = False # adjacent node has no crow
        
        if res: self.winner = 0
        return res
    
    
    def declare_winner(self):
        winner = "Vulture" if self.winner == 1 else "Crows"
        self.text = self.font.render(f"Winner: {winner}", True, (0, 0, 0)) 
        text_rect = self.text.get_rect()
        text_rect.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)

        self.screen.blit(self.text, text_rect)

        print(f"winner : {self.winner}")

    def run_game(self):
        
        while self.run:
            self.process_board()
            if self.winner != -1 : break
            for event in pygame.event.get():
                if self.check_win():
                    self.declare_winner()
                    self.run = False
                    break   
                if event.type == pygame.QUIT or self.winner != -1:
                    self.run = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"x,y = {event.pos}")
                    circle = self.get_circle(event.pos)
                    print(f"Got center {self.get_circle(event.pos)}")
                   
                    if circle is None: continue
                    x = 0
                    if self.turn == 1: 
                        x = self.vulture_turn(circle)
                        self.turn = 1 - x

                    elif self.turn == 0:
                        self.crow_turn(circle)
                        
                    elif self.turn == -1:
                        self.buffer_turn(circle)
                        

            
            pygame.display.flip()
    
    def vulture_turn(self, circle):
        # circle already filled
        if circle in self.circles: return 0

        
        if self.vulture is None: # first move
            self.vulture = circle 
            self.add_circle(circle)
            return 1

        # self.can_kill()
        if self.kill is not None:
            if circle != self.kill[1]: return 0
            self.kill_crow(circle)
            return 1

        # adjacent vertex
        curr_idx = self.cords.index(self.vulture)
        for node in graph[curr_idx]:
            node_circle = self.cords[node]
            if node_circle not in self.circles and node_circle == circle:
                print(f"shifted from {curr_idx} to {node}")
                self.circles.remove(self.vulture)
                self.add_circle(circle)
                self.vulture = circle
                return 1
        
        # add kill 
        return 0

    def crow_turn(self, circle):
        if circle not in self.circles and self.crows  > 0:
                self.add_circle(circle)
                self.turn = 1
                self.crows -= 1
                if self.vulture is not None: self.can_kill()

        elif circle not in self.circles and self.crows == 0:
            self.turn = 0
        elif circle in self.circles and self.crows != 0: # only remove circles if there are no crows remaining
            self.turn = 0
        elif circle == self.vulture: self.turn = 0 # vultures spot
        else:
            self.turn = -1 #create backup
            self.backup_circles = self.circles
            self.removed_circle = circle
            self.circles.remove(circle)
    
       
    def buffer_turn(self, circle):
        adjacent = self.adjacent(circle, self.removed_circle)
        if circle not in self.circles and adjacent:
            self.add_circle(circle)
            self.turn = 1
            if self.vulture is not None: self.can_kill()
        else: #restore backup
            self.circles = self.backup_circles
            self.add_circle(self.removed_circle)
            self.turn = 0
                           

    def kill_crow(self, circle):
        crow, vulture = self.kill[0], self.kill[1]
        self.circles.remove(crow)
        self.circles.remove(self.vulture)
        self.add_circle(vulture)
        self.vulture = vulture
        self.kill = None
        self.vulture_score += 1

    def dfs(self, origin, curr, depth):
        if depth == 1 and (curr in jump[origin]): return True
        if depth >= 1: return False
        for adj in graph[curr]:
            if self.cords[adj] in self.circles: continue
            if self.dfs(origin, adj, depth + 1) : return adj
        return False



    def can_kill(self):
        node = self.cords.index(self.vulture)
        for adj in graph[node]:
            if self.cords[adj] in self.circles:
                val = self.dfs(node, adj, 0)
                if val:
                    self.kill = (self.cords[adj], self.cords[val])
                    print(f"Can kill {node} to {adj} to {val}")


    def quit(self):
        pygame.quit()

game = Game()
game.run_game()
if game.winner != -1: sleep(5)
game.quit()

# edge case when putting same crow on same position after all 7