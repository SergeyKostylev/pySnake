import pygame
from pygame import Rect
import constants as c
import time
import itertools


class Snake:
    DIRECTION_UP = 'up'
    DIRECTION_DOWN = 'down'
    DIRECTION_LEFT = 'left'
    DIRECTION_RIGHT = 'right'

    BODY_SIZE = c.SNAKE_BODY_PIECE_SIZE

    def __init__(self, length: int = 11, position=(300, 300), direction=DIRECTION_RIGHT):
        self._body: list[Rect] = []
        self._validate_direction(direction)
        self._length = length
        self._direction = direction
        self._create_snake(position[0], position[1])
        self._last_time = time.time()

    def get_body(self):
        seconds = int(time.time() - self._last_time) * 1

        if seconds == 0:  # changer nothing
            return self._body

        x, y = [0, 0]
        match self._direction:
            case self.DIRECTION_UP:
                y = -c.SNAKE_BODY_PIECE_SIZE
            case self.DIRECTION_DOWN:
                y = c.SNAKE_BODY_PIECE_SIZE
            case self.DIRECTION_LEFT:
                x = -c.SNAKE_BODY_PIECE_SIZE
            case self.DIRECTION_RIGHT:
                x = c.SNAKE_BODY_PIECE_SIZE
            case _:
                ValueError(f"Invalid direction '{self._direction}'")

        for _ in range(seconds):
            position = len(self._body)
            for _ in range(len(self._body) - 1, -1, -1):  # loop from tail to head
                position = position - 1
                if position == 0:  # is header
                    self._body[position].move_ip(x, y)
                else:
                    self._body[position].topleft = (self._body[position - 1].x, self._body[position - 1].y)

            if self.snake_intersection():
                pass  # TODO: game over

        self._last_time = time.time()

        return self._body

    def set_direction(self, direction):
        self._validate_direction(direction)

        common_and_pretend = sorted([self._direction, direction])
        mutually_exclusive = [
            sorted([self.DIRECTION_UP, self.DIRECTION_DOWN]),
            sorted([self.DIRECTION_LEFT, self.DIRECTION_RIGHT]),
        ]

        for pair in mutually_exclusive:
            if common_and_pretend == pair:
                return  # can't switch up -> down, down -> up, ...

        self._direction = direction
        print(direction)

    def snake_intersection(self)-> bool:
        for rect1, rect2 in itertools.combinations(self._body, 2):
            if rect1.colliderect(rect2):
                return True
        return False

    def _create_snake(self, head_x, head_y):
        self._body = [
            self._get_new_snake_piece(head_x, head_y)
        ]

        loop_x, loop_y = [head_x, head_y]

        for _ in range(self._length - 1):
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
