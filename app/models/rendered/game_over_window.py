import sys
import time

import pygame
from pygame import Rect

from app import configuration as conf

from app.models.rendered.base_rendered_model import BaseRenderedModel


class GameOverWindow(BaseRenderedModel):

    __text = "GAME OVER"
    def __init__(self):
        self.__window = self.__build()


    def __build(self):
        width, height = conf.DIALOG_WINDOW_SIZE
        x = (conf.SCREEN_SIZE[0] - width) // 2
        y = (conf.SCREEN_SIZE[1] - height) // 2

        return Rect(x, y, width, height)

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, conf.DIALOG_WINDOW_COLOR, self.__window)

    def start_new_game(self) -> bool:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_y:
                            return True
                        case pygame.K_n:
                            return False
