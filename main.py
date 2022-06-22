import pygame
import time

pygame.init()
pygame.font.init()
class GridBox:
    def __init__(self, index):
        self.index = index
        self.x = (index%3)*150
        self.y = index//3*150
        self.width = 150
        self.height = 150
        self.typ = None
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.assets = [
            pygame.image.load("assets/o.png"),
            pygame.image.load("assets/x.png"),
        ]

    def update(self, current, turn=False):
        if current is None:
            return
        if turn:
            self.typ = current
        if self.typ is None:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.typ = current
                    return True

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((450, 550))
        pygame.display.set_caption("Tic-Tac-Toe AI")
        self.CLOCK = pygame.time.Clock()
        self.RUNNING = True

        self.game_grid = [[0]*3, [0]*3, [0]*3]
        for i in range(9):
            self.game_grid[i//3][(i%3)] = GridBox(i)

        self.current = 0
        self.win = False
        self.win_line = []
        self.current_scene = "menu"

        self.PINK = (241, 99, 122)
        self.BLUE = (22, 157, 200)
        self.TOPLEVEL = (158, 140, 104)
        self.grid = pygame.image.load("assets/grid.png")
        self.home = pygame.image.load("assets/home.png")

    def check_win(self):
        combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        flat_grid = []
        for y in self.game_grid:
            for x in y:
                flat_grid.append(x)
        for c in combinations:
            if flat_grid[c[0]].typ == flat_grid[c[1]].typ == flat_grid[c[2]].typ != None:
                self.win_line.append((flat_grid[c[0]].x+75, flat_grid[c[0]].y+75))
                self.win_line.append((flat_grid[c[2]].x+75, flat_grid[c[2]].y+75))
                return str(flat_grid[c[0]].typ)
        return False

    def display_info(self):
        player = "O" if self.current == 0 else "X"

        if self.win:
            player = "O" if self.current == 1 else "X"
            text = f"{player} Won!"
        else:
            text = f"{player}'s Turn"

        text_element = pygame.font.SysFont("comicsans", 35).render(text, True, self.TOPLEVEL)
        text_rect = text_element.get_rect()
        text_rect.center = (450/2, 500)
        self.screen.blit(text_element, text_rect)
    
    def restart(self):
        self.game_grid = [[0]*3, [0]*3, [0]*3]
        for i in range(9):
            self.game_grid[i//3][(i%3)] = GridBox(i)

        self.current = 0
        self.win = False
        self.win_line = []
    
    def player_vs_player(self):
        self.screen.blit(self.grid, (0, 0))
        for y in self.game_grid:
            for x in y:
                e = x.update(self.current if not self.win else None)
                if e:
                    self.current = 1 if self.current == 0 else 0
                    win = self.check_win()
                    if win:
                        p = ["O", "X"]
                        print(f"{p[int(win)]} Won!")
                        self.win = True
                if x.typ != None:
                    self.screen.blit(x.assets[x.typ], (x.x, x.y))
        self.display_info()
        if self.win:
            pygame.draw.line(self.screen, self.TOPLEVEL, self.win_line[0], self.win_line[1], 8)
        back_btn = pygame.Rect(15, 490, 90, 50)
        if back_btn.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.current_scene = "menu"

    def menu(self):
        self.screen.blit(self.home, (0, 0))
        btn_1 = pygame.Rect(100, 315, 250, 70)
        btn_2 = pygame.Rect(100, 400, 250, 70)
        if btn_1.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.5)
                self.restart()
                self.current_scene = "pvp"

    def run(self):
        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
            self.screen.fill((255, 255, 255))
            if self.current_scene == "menu":
                self.menu()
            elif self.current_scene == "pvp":
                self.player_vs_player()
            self.CLOCK.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game= Game()
    game.run()