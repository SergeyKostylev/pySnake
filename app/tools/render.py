import pygame
from app import configuration as c

from app.models.game_area import GameArea
from app.models.rendered.info_bar import InfoBar


class Render:
    def __init__(self, game_area: GameArea, info_bar: InfoBar, screen):
        self.__screen = screen
        self.__game_area = game_area
        self.__info_bar = info_bar

    def render(self):
        screen = self.__screen
        snake_field, snake, target = self.__game_area.get_all_entities()

        screen.fill(c.SCREEN_BACKGROUND_COLOR)

        snake_field.render(screen)
        target.render(screen)
        snake.render(screen)

        self.__info_bar.render(screen)

        pygame.display.flip()