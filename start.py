import pygame
import configuration as c
import sys
from app.game_area import GameArea

pygame.init()

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

    keydown_event.clear()


def render(game_area: GameArea):
    screen, snake_field, snake, target = game_area.get_all_entities()

    screen.fill(c.SCREEN_BACKGROUND_COLOR)

    pygame.draw.rect(screen, c.SNAKE_FIELD_COLOR, snake_field.field)

    for rec in snake.get_body():
        pygame.draw.rect(screen, c.SNAKE_COLOR, rec)

    pygame.display.flip()
    # pygame.display.update()
    # print(keydown_event)

    pass


def run():
    game_area = GameArea()

    while True:
        processInput()
        update(game_area)
        render(game_area)


if __name__ == '__main__':
    run()
