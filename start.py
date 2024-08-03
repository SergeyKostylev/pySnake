import pygame

import configuration as c
import sys

from app.render import Render
from models.game_area import GameArea


keydown_event = []

def processInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event.append(event.key)


def update(game_area: GameArea):
    snake = game_area.snake

    for event_key in keydown_event:
        command = None
        if event_key == pygame.K_UP:
            command = snake.DIRECTION_UP
        elif event_key == pygame.K_DOWN:
            command = snake.DIRECTION_DOWN
        elif event_key == pygame.K_LEFT:
            command = snake.DIRECTION_LEFT
        elif event_key == pygame.K_RIGHT:
            command = snake.DIRECTION_RIGHT

        if command is not None:
            snake.set_direction(command)

    game_area.check_updates()

    keydown_event.clear()



def run():
    screen = pygame.display.set_mode(c.SCREEN_SIZE)
    game_area = GameArea()
    render = Render(game_area, screen)

    while True:
        processInput()
        update(game_area)

        if game_area.game_over:
            exit()

        render.render()


if __name__ == '__main__':
    c.validate_configuration()


    pygame.init()
    run()
