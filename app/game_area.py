import pygame
import configuration as const
from models.snake import Snake
from models.snake_field import SnakeField
from exceptions.exceptions import ConfigValueException
from models.target import Target


class GameArea:
    def __init__(self):
        self.__validate_config()
        self.__snake_field = self.__get_snake_field()
        self.__screen = pygame.display.set_mode(const.SCREEN_SIZE)
        self.__snake = self.__build_snake()
        self.__target = self.__build_target()

    def get_all_entities(self):
        return self.__screen, self.__snake_field, self.__snake, self.__target

    @property
    def snake(self):
        return self.__snake

    def __build_target(self) -> Target:


        x = 100
        y = 100

        return Target(x, y)

    def __build_snake(self) -> Snake:
        snake_field_center_position = self.__snake_field.get_center_point()

        snake_field_center_position = (  # TODO: remove after testing FOR
            snake_field_center_position[0] + 100,
            snake_field_center_position[1]
        )

        return Snake(position=snake_field_center_position)

    def __get_snake_field(self) -> SnakeField:
        screen_size = const.SCREEN_SIZE
        field_size = const.SNAKE_FIELD_SIZE
        # x = (screen_size[0] - field_size[0]) // 2
        x = 20  # temporary  solution
        y = (screen_size[1] - field_size[1]) // 2

        return SnakeField(const.SNAKE_FIELD_SIZE[0], const.SNAKE_FIELD_SIZE[1], x, y)

    def __validate_config(self) -> None:
        screen_size = const.SCREEN_SIZE
        snake_field_size = const.SNAKE_FIELD_SIZE
        if screen_size[0] <= snake_field_size[0]:
            raise ConfigValueException("Screen width must be greater than snake field width")
        if screen_size[1] <= snake_field_size[1]:
            raise ConfigValueException("Screen height must be greater than snake field height")

        # TODO: check snake_field_size % SNAKE_BODY_PIECE_SIZE = 0
