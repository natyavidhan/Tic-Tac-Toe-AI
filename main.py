import pygame

class GridBox:
    def __init__(self, index):
        self.index = index
        self.x = (index%3)*150
        self.y = index//3*150
        self.width = 150
        self.height = 150
        self.typ = None
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.width, self.height), 3, 15)
        self.center_rect = pygame.Rect(0, 0, 120, 120)
        self.center_rect.center = (self.width/2, self.height/2)

        self.assets = [
            pygame.transform.scale(pygame.image.load("assets/o.png"), (120, 120)),
            pygame.transform.scale(pygame.image.load("assets/x.png"), (120, 120)),
        ]
        self.surface.fill((255, 255, 255))

    def update(self, current):
        self.surface.fill((255, 255, 255))
        if self.typ is None:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.typ = current
                    return True
        if self.typ is not None:
            self.surface.blit(self.assets[self.typ], (self.center_rect.x, self.center_rect.y))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((450, 550))
        pygame.display.set_caption("Tic-Tac-Toe AI")
        self.CLOCK = pygame.time.Clock()
        self.RUNNING = True

        self.game_grid = [[0]*3, [0]*3, [0]*3]
        for i in range(9):
            self.game_grid[i//3][(i%3)] = GridBox(i)
        print(self.game_grid)
        self.current = 0

    def run(self):
        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False
            self.screen.fill((255, 255, 255))
            for y in self.game_grid:
                for x in y:
                    e = x.update(self.current)
                    if e:
                        self.current = 1 if self.current == 0 else 0
                    self.screen.blit(x.surface, (x.x, x.y))
            self.CLOCK.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    game= Game()
    game.run()