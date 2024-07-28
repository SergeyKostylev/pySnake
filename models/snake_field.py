from pygame import Rect


class SnakeField:

    def __init__(self, width: int, height: int,  x: int, y: int):
        self.__field = Rect(x, y, width, height)

    @property
    def field(self) -> Rect:
        return self.__field

    def get_center_point(self):
        return (
            self.field.width // 2 + self.field.x,
            self.field.height // 2 + self.field.y
        )
