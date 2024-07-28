from pygame import Rect

import configuration


class Target:
    TARGET_SIZE = configuration.TARGET_SIZE

    def __init__(self, x, y):
        self.__target = Rect(x, y, self.TARGET_SIZE, self.TARGET_SIZE)

    def move(self, x, y):
        self.__target.move_ip(x, y)
