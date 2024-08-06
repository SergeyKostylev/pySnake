import pygame
from pygame import Rect
from app import configuration as conf

from app.models.rendered.base_rendered_model import BaseRenderedModel


class GameOverWindow(BaseRenderedModel):

    def __init__(self):
        self.__window = self.__build()

    def __build(self):
        width, height = conf.DIALOG_WINDOW_SIZE
        x = (conf.SCREEN_SIZE[0] - width) // 2
        y = (conf.SCREEN_SIZE[1] - height) // 2

        return Rect(x, y, width, height)

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, conf.DIALOG_WINDOW_COLOR, self.__window)

        texts = [
            "GAME OVER",
            "Press N to quit",
            "Press Y to start a new game"
        ]

        font = pygame.font.SysFont('Arial', conf.INFO_BAR_TEXT_SIZE)
        y_shift = 0
        for text in texts:
            surface = font.render(text, True, conf.DIALOG_WINDOW_TEXT_COLOR)
            x_center = self.__window.x + (self.__window.width // 2) - (surface.get_rect().width // 2)
            screen.blit(surface, (x_center, self.__window.y + y_shift))
            y_shift += conf.INFO_BAR_TEXT_SIZE

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
