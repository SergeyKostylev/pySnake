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

    snake_field_center_position = (  # TODO: remove after testing FOR
        snake_field_center_position[0] + 120,
        snake_field_center_position[1]
    )

    return Snake(position=snake_field_center_position)


def build_snake_field() -> SnakeField:
    screen_size = conf.SCREEN_SIZE
    field_size = conf.SNAKE_FIELD_SIZE
    # x = (screen_size[0] - field_size[0]) // 2 TODO: for test only
    x = 20  # temporary  solution
    y = (screen_size[1] - field_size[1]) // 2

    return SnakeField(conf.SNAKE_FIELD_SIZE[0], conf.SNAKE_FIELD_SIZE[1], x, y)


def build_target(point: tuple[int, int]) -> Target:
    return Target(point[0], point[1])
