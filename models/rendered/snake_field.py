import pygame
from pygame import Rect
import configuration as c


from models.rendered.base_rendered_model import BaseRenderedModel


class SnakeField(BaseRenderedModel):

    def __init__(self, width: int, height: int,  x: int, y: int):
        self.__field = Rect(x, y, width, height)

    def render(self, screen):
        pygame.draw.rect(screen, c.SNAKE_FIELD_COLOR, self.__field)


    @property
    def field(self) -> Rect:
        return self.__field

    def get_center_point(self):
        return (
            self.field.width // 2 + self.field.x,
            self.field.height // 2 + self.field.y
        )
