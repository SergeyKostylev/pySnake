from pygame import Rect

import configuration


class Target:
    TARGET_SIZE = configuration.FIELD_POINT_SIZE

    def __init__(self, x, y):
        self.__body = Rect(x, y, self.TARGET_SIZE, self.TARGET_SIZE)

    @property
    def body(self):
        return self.__body
