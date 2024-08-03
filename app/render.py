import pygame
import configuration as c

from models.game_area import GameArea


class Render:
    def __init__(self, game_area: GameArea, screen):
        self.__screen = screen
        self.__game_area = game_area

    def render(self):
        screen = self.__screen
        snake_field, snake, target = self.__game_area.get_all_entities()

        screen.fill(c.SCREEN_BACKGROUND_COLOR)

        snake_field.render(screen)
        target.render(screen)
        snake.render(screen)

        pygame.display.flip()
        # pygame.display.update()
        # print(keydown_event)
