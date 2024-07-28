from pygame import Rect


class SnakeField:

    def __init__(self, height: int, width: int, x: int, y: int):
        self.__field = Rect(x, y, width, height)

    @property
    def field(self) -> Rect:
        return self.__field
