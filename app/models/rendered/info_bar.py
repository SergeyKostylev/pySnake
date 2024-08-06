from time import time
from datetime import datetime
import pygame
from pygame import Rect
from app import configuration as conf
from app.models.rendered.base_rendered_model import BaseRenderedModel


class InfoBar(BaseRenderedModel):

    def __init__(self, width: int, height: int, x: int, y: int):
        self.__field = Rect(x, y, width, height)
        self.__time_start = time()
        self.__targets_amount = 0
        self.__speed = 0
        self.__font = pygame.font.SysFont('Arial', conf.INFO_BAR_TEXT_SIZE)

    def render(self, screen: pygame.Surface):
        self.__render_text(screen)

        pygame.draw.rect(screen, conf.INFO_BAR_COLOR_BORDER, self.__field, 1)

    def __render_text(self, screen: pygame.Surface):
        game_time = datetime.fromtimestamp(time() - self.__time_start).strftime('%M:%S')  # ('%M:%S.%f')[:-5]
        texts = [
            f"{game_time}",
            f"x {self.__targets_amount}",
            f"speed: {self.__speed}",
        ]

        y_shift = 0
        for text in texts:
            surface = self.__font.render(text, True, conf.INFO_BAR_COLOR_TEXT)
            x_center = self.__field.x + (self.__field.width // 2) - (surface.get_rect().width // 2)
            screen.blit(surface, (x_center, self.__field.y + y_shift))
            y_shift += conf.INFO_BAR_TEXT_SIZE

    def set_target_amount(self, value: int):
        self.__targets_amount = value

    def set_speed(self, value):
        self.__speed = value

    @property
    def field(self) -> Rect:
        return self.__field
