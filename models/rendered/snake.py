import copy

import pygame
from pygame import Rect
import configuration as c

from models.rendered.base_rendered_model import BaseRenderedModel


class Snake(BaseRenderedModel):
    DIRECTION_UP = 'up'
    DIRECTION_DOWN = 'down'
    DIRECTION_LEFT = 'left'
    DIRECTION_RIGHT = 'right'

    PIECE_SIZE = c.FIELD_POINT_SIZE

    def __init__(self, length: int = 10, position=(300, 300), direction=DIRECTION_RIGHT):
        self.__body: list[Rect] = []
        self.__validate_direction(direction)
        self.__direction = direction
        self.__requested_directions = []
        self.__create_body(position[0], position[1], length)
        self.__speed = 300

    def render(self, screen: pygame.Surface):
        for rec in self.__body:
            pygame.draw.rect(screen, c.SNAKE_COLOR, rec)

    def grow(self):
        self.__body.append(
            copy.deepcopy(self.__body[-1])
        )

    @property
    def speed(self):
        return self.__speed

    def do_step(self):

        if len(self.__requested_directions) > 0:
            direction = self.__requested_directions.pop(0)
        else:
            direction = self.__direction

        x, y = [0, 0]
        match direction:
            case self.DIRECTION_UP:
                y = -self.PIECE_SIZE
            case self.DIRECTION_DOWN:
                y = self.PIECE_SIZE
            case self.DIRECTION_LEFT:
                x = -self.PIECE_SIZE
            case self.DIRECTION_RIGHT:
                x = self.PIECE_SIZE
            case _:
                ValueError(f"Invalid direction '{self.__direction}'")

        tail = self.__body.pop()
        tail.x = self.__body[0].x + x
        tail.y = self.__body[0].y + y
        self.__body.insert(0, tail)

        self.__direction = direction
        pass

    @property
    def body(self):
        return self.__body

    def set_direction(self, direction):
        requested_directions_len = len(self.__requested_directions)
        if requested_directions_len >= 2:
            return

        self.__validate_direction(direction)
        previous_direction = self.__requested_directions[0] if requested_directions_len > 0 else self.__direction

        if self.__is_opposite_directions(previous_direction, direction):
            return

        self.__requested_directions.append(direction)

    def __is_opposite_directions(self, directionOne, directionTwo):
        common_and_pretend = sorted([directionOne, directionTwo])
        mutually_exclusive = [
            sorted([self.DIRECTION_UP, self.DIRECTION_DOWN]),
            sorted([self.DIRECTION_LEFT, self.DIRECTION_RIGHT]),
        ]

        for pair in mutually_exclusive:
            if common_and_pretend == pair:
                return True  # can't switch up -> down, down -> up, ...

        return False

    def snake_intersection(self) -> bool:
        head = self.__body[0]
        for i in range(1, len(self.__body)):
            if head.colliderect(self.__body[i]):
                return True

        return False

    def __create_body(self, head_x: int, head_y: int, length: int):
        self.__body = [
            self.__get_new_snake_piece(head_x, head_y)
        ]

        loop_x, loop_y = [head_x, head_y]

        for _ in range(length - 1):
            match self.__direction:
                case self.DIRECTION_UP:
                    loop_y = loop_y + self.PIECE_SIZE
                case self.DIRECTION_DOWN:
                    loop_y = loop_y - self.PIECE_SIZE
                case self.DIRECTION_LEFT:
                    loop_x = loop_x + self.PIECE_SIZE
                case self.DIRECTION_RIGHT:
                    loop_x = loop_x - self.PIECE_SIZE
                case _:
                    ValueError(f"Invalid direction '{self.__direction}'")

            self.__body.append(
                self.__get_new_snake_piece(loop_x, loop_y)
            )

    def __get_new_snake_piece(self, x, y):
        return Rect(x, y, self.PIECE_SIZE, self.PIECE_SIZE)

    def __validate_direction(self, direction):
        if direction not in [self.DIRECTION_UP, self.DIRECTION_DOWN, self.DIRECTION_LEFT, self.DIRECTION_RIGHT]:
            raise ValueError(f"Invalid direction '{direction}'")


if __name__ == '__main__':
    pass
