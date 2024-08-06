import pygame
from app import configuration as c

from app.models.rendered.base_rendered_model import BaseRenderedModel


class Render:
    def __init__(self, screen: pygame.Surface):
        self.__screen = screen

    @property
    def screen(self):
        return self.__screen

    def fill_background(self):
        self.__screen.fill(c.SCREEN_BACKGROUND_COLOR)

        return self

    def render(self, *args: BaseRenderedModel):
        for model in args:
            model.render(self.__screen)

        return self

    def flip_display(self):
        pygame.display.flip()
