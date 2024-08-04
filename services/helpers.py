import random

import configuration as conf
from models.rendered.snake import Snake
from models.rendered.target import Target
from models.rendered.snake_field import SnakeField


def get_random_empy_field_point(snake_field: SnakeField, snake: Snake = None, target: Target = None) -> tuple[int, int]:
    snake_field_rect = snake_field.field
    field_x_from = snake_field_rect.x
    field_y_from = snake_field_rect.y
    field_x_to = snake_field_rect.width + field_x_from
    field_y_to = snake_field_rect.height + field_y_from

    filled_filed_points = [] if target is None else [(target.body.x, target.body.x)]

    if snake is not None:
        for piece in snake.body:
            filled_filed_points.append((piece.x, piece.y))

    empty_filed_points = []
    for i in range(field_x_from, field_x_to, conf.FIELD_POINT_SIZE):
        for j in range(field_y_from, field_y_to, conf.FIELD_POINT_SIZE):
            point = (i, j)
            if point not in filled_filed_points:
                empty_filed_points.append(point)

    return random.choice(empty_filed_points)
