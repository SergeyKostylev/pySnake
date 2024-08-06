import pygame
from pygame import Rect
from app import configuration as c, configuration

from app.models.rendered.base_rendered_model import BaseRenderedModel


class Target(BaseRenderedModel):
    TARGET_SIZE = configuration.FIELD_POINT_SIZE

    def __init__(self, x, y):
        self.__body = Rect(x, y, self.TARGET_SIZE, self.TARGET_SIZE)

    @property
    def body(self):
        return self.__body

    def render(self, screen):
        pygame.draw.rect(screen, c.TARGET_COLOR, self.__body)
