import pygame


class Grid:
    def __init__(self, height, width):
        self.black = (0, 0, 0)
        self.white = (200, 200, 200)
        self.height = height
        self.width = width
        self.screen = None
        self.clock = None

    def initialise_grid_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.screen.fill(self.white)

    def drawgrid(self):
        block_size = 20
        for x in range(0, self.width, block_size):
            for y in range(0, self.height, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(self.screen, self.black, rect, 1)
