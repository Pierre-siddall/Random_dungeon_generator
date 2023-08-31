import random
import sys
import pygame
import grid


def roll(die_number, side_number):
    if die_number == 1:
        result = random.randint(1, side_number)
    elif die_number > 1:
        results = []
        for x in range(die_number):
            results.append(random.randint(1, side_number))


def main():
    map = grid.Grid(1000,1700)

    map.initialise_grid_window()

    while True:
        map.drawgrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
