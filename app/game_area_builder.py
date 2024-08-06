from models.game_area import GameArea
from models.rendered.info_bar import InfoBar
from models.rendered.snake import Snake
from models.rendered.snake_field import SnakeField

import configuration as conf
from models.rendered.target import Target
from services.helpers import get_random_empy_field_point


def build_game_area() -> GameArea:
    snake_field = build_snake_field()
    snake = build_snake(snake_field)

    point = get_random_empy_field_point(snake_field, snake)
    target = build_target(point)

    return GameArea(snake, snake_field, target)


def build_snake(snake_field: SnakeField) -> Snake:
    snake_field_center_position = snake_field.get_center_point()

    position = (
        round_to_point_size(snake_field_center_position[0]),
        round_to_point_size(snake_field_center_position[1])
    )

    return Snake(position=position)


def build_snake_field() -> SnakeField:
    x = get_x_for_snake_field()
    y = get_y_for_snake_field_and_info_bar()

    return SnakeField(conf.SNAKE_FIELD_SIZE[0], conf.SNAKE_FIELD_SIZE[1], x, y)


def build_target(point: tuple[int, int]) -> Target:
    return Target(
        round_to_point_size(point[0]),
        round_to_point_size(point[1])
    )


def build_info_bar() -> InfoBar:
    y = get_y_for_snake_field_and_info_bar()

    snake_field_x_left = get_x_for_snake_field()
    snake_field_x_right = conf.SNAKE_FIELD_SIZE[0] + snake_field_x_left
    empty_size = (conf.SCREEN_SIZE[0] - snake_field_x_right - conf.INFO_BAR_SIZE[0])
    x = snake_field_x_right + (empty_size - snake_field_x_left)

    return InfoBar(conf.INFO_BAR_SIZE[0], conf.INFO_BAR_SIZE[1], x, y)


def get_x_for_snake_field() -> int:
    width_sum = conf.SNAKE_FIELD_SIZE[0] + conf.INFO_BAR_SIZE[0]
    return round_to_point_size((conf.SCREEN_SIZE[0] - width_sum) / 3)


def get_y_for_snake_field_and_info_bar() -> int:
    return round_to_point_size((conf.SCREEN_SIZE[1] - conf.SNAKE_FIELD_SIZE[1]) // 2)


def round_to_point_size(value):
    return int((value // conf.FIELD_POINT_SIZE) * conf.FIELD_POINT_SIZE)
