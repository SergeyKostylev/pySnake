import pygame
from abc import ABC, abstractmethod


class BaseRenderedModel(ABC):

    @abstractmethod
    def render(self, screen: pygame.Surface):
        pass
