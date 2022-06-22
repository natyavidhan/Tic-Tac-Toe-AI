import pygame

class GridBox:
    def __init__(self, index):
        self.index = index
        self.x = (index%3)*220
        self.y = index//3*220
        self.width = 220
        self.height = 220
        self.typ = None
        self.surface = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.width, self.height), 2, 15)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 660))
        pygame.display.set_caption("Tic-Tac-Toe AI")
        self.CLOCK = pygame.time.Clock()
        self.RUNNING = True

        self.game_grid = [[0]*3, [0]*3, [0]*3]
        print(self.game_grid)
        for i in range(9):
            self.game_grid[i//3][(i%3)] = GridBox(i)
        self.current = 0

    def make_move(self, index):
        if self.game_grid[index[0]][index[1]] is None:
            self.game_grid[index[0]][index[1]] = self.current

    def run(self):
        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False

if __name__ == "__main__":
    game= Game()