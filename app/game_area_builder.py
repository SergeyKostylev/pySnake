from models.game_area import GameArea
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
    screen_size = conf.SCREEN_SIZE
    field_size = conf.SNAKE_FIELD_SIZE
    # x = round_to_point_size((screen_size[0] - field_size[0]) // 2) TODO: for test only
    x = 20  # temporary  solution
    y = round_to_point_size((screen_size[1] - field_size[1]) // 2)

    return SnakeField(conf.SNAKE_FIELD_SIZE[0], conf.SNAKE_FIELD_SIZE[1], x, y)


def build_target(point: tuple[int, int]) -> Target:
    return Target(
        round_to_point_size(point[0]),
        round_to_point_size(point[1])
    )


def round_to_point_size(value):
    return (value // conf.FIELD_POINT_SIZE) * conf.FIELD_POINT_SIZE