import pygame
from pygame import Rect
import configuration as c
import time
import itertools

from exceptions.exceptions import GameOverException


class Snake:
    DIRECTION_UP = 'up'
    DIRECTION_DOWN = 'down'
    DIRECTION_LEFT = 'left'
    DIRECTION_RIGHT = 'right'

    PIECE_SIZE = c.SNAKE_BODY_PIECE_SIZE

    def __init__(self, length: int = 3, position=(300, 300), direction=DIRECTION_RIGHT):
        self.__body: list[Rect] = []
        self.__validate_direction(direction)
        self.__length = length
        self.__direction = direction
        self.__create_snake(position[0], position[1])
        self.__last_time = time.time()

    @property
    def length(self):
        return self.__length
    @property
    def body(self):
        steps = int(time.time() - self.__last_time)

        if steps == 0:  # changer nothing
            return self.__body

        x, y = [0, 0]
        match self.__direction:
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

        for _ in range(steps):
            position = len(self.__body) # TODO: need to edit logic and move tail piece (to head) only
            for _ in range(len(self.__body) - 1, -1, -1):  # loop from tail to head
                position = position - 1
                if position == 0:  # is header
                    self.__body[position].move_ip(x, y)
                else:
                    self.__body[position].topleft = (self.__body[position - 1].x, self.__body[position - 1].y)

            if self.snake_intersection():
                # raise GameOverException()
                pass  # TODO: game over

        self.__last_time = time.time()

        return self.__body

    def set_direction(self, direction):
        self.__validate_direction(direction)

        common_and_pretend = sorted([self.__direction, direction])
        mutually_exclusive = [
            sorted([self.DIRECTION_UP, self.DIRECTION_DOWN]),
            sorted([self.DIRECTION_LEFT, self.DIRECTION_RIGHT]),
        ]

        for pair in mutually_exclusive:
            if common_and_pretend == pair:
                return  # can't switch up -> down, down -> up, ...

        self.__direction = direction
        print(direction)

    def snake_intersection(self) -> bool:

        head = self.__body[0]
        for i in range(1, len(self.__body)):
            if head.colliderect(self.__body[i]):
                return True

        # for rect1, rect2 in itertools.combinations(self._body, 2):
        #     if rect1.colliderect(rect2):
        #         return True
        return False

    def __create_snake(self, head_x, head_y):
        self.__body = [
            self.__get_new_snake_piece(head_x, head_y)
        ]

        loop_x, loop_y = [head_x, head_y]

        for _ in range(self.__length - 1):
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
