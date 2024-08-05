import pygame


class GameAreaState:
    def __init__(self):
        self.__last_snake_moving_time = pygame.time.get_ticks()

    def update_last_snake_moving_time(self):
        self.__last_snake_moving_time = pygame.time.get_ticks()

    @property
    def last_snake_moving_time(self):
        return self.__last_snake_moving_time
