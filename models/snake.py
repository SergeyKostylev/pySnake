import pygame
from pygame import Rect
import constants as c
import time


class Snake:
    DIRECTION_UP = 'up'
    DIRECTION_DOWN = 'down'
    DIRECTION_LEFT = 'left'
    DIRECTION_RIGHT = 'right'

    BODY_SIZE = c.SNAKE_BODY_PIECE_SIZE

    def __init__(self, length: int = 11, position=(300, 300), direction=DIRECTION_RIGHT):
        self._body: list[Rect] = []
        self._validate_direction(direction)
        self.length = length
        self._direction = direction
        self._create_snake(position[0], position[1])
        self.last_time = time.time()

    def get_body(self):
        seconds = int(time.time() - self.last_time)

        if seconds == 0:  # changer nothing
            return self._body

        value = seconds * c.SNAKE_BODY_PIECE_SIZE
        x, y = [0, 0]

        match self._direction:
            case self.DIRECTION_UP:
                y = -value
            case self.DIRECTION_DOWN:
                y = value
            case self.DIRECTION_LEFT:
                x = -value
            case self.DIRECTION_RIGHT:
                x = value
            case _:
                ValueError(f"Invalid direction '{self._direction}'")

        position = len(self._body)
        for _ in range(len(self._body) - 1, -1, -1):  # loop from tail to head
            position = position - 1
            if position == 0:  # is header
                self._body[position].move_ip(x, y)
            else:
                self._body[position].topleft = (self._body[position - 1].x, self._body[position - 1].y)

        self.last_time = time.time()

        return self._body

    def set_direction(self, direction):
        self._validate_direction(direction)
        self._direction = direction
        print(direction)

    def _create_snake(self, head_x, head_y):
        self._body = [
            self._get_new_snake_piece(head_x, head_y)
        ]

        loop_x, loop_y = [head_x, head_y]

        for _ in range(self.length - 1):
            match self._direction:
                case self.DIRECTION_UP:
                    loop_y = loop_y + c.SNAKE_BODY_PIECE_SIZE
                case self.DIRECTION_DOWN:
                    loop_y = loop_y - c.SNAKE_BODY_PIECE_SIZE
                case self.DIRECTION_LEFT:
                    loop_x = loop_x + c.SNAKE_BODY_PIECE_SIZE
                case self.DIRECTION_RIGHT:
                    loop_x = loop_x - c.SNAKE_BODY_PIECE_SIZE
                case _:
                    ValueError(f"Invalid direction '{self._direction}'")

            self._body.append(
                self._get_new_snake_piece(loop_x, loop_y)
            )

    def _get_new_snake_piece(self, x, y):
        return Rect(x, y, self.BODY_SIZE, self.BODY_SIZE)

    def _validate_direction(self, direction):
        if direction not in [self.DIRECTION_UP, self.DIRECTION_DOWN, self.DIRECTION_LEFT, self.DIRECTION_RIGHT]:
            raise ValueError(f"Invalid direction '{direction}'")


if __name__ == '__main__':
    pass
