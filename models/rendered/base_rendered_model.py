from abc import ABC, abstractmethod

import pygame


class BaseRenderedModel(ABC):

    @abstractmethod
    def render(self, screen: pygame.Surface):
        pass