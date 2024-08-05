import sys

import pygame
import configuration as conf
from app.game_area_builder import build_game_area
from app.render import Render
from models.game_area import GameArea
from models.rendered.snake import Snake


class App:
    interval = 1000 // conf.FPS

    def __init__(self):
        self.__snake_command_buf = []

        pass

    def run(self):
        conf.validate_configuration()
        pygame.init()
        screen = pygame.display.set_mode(conf.SCREEN_SIZE)

        game_area = build_game_area()
        render = Render(game_area, screen)

        threshold = pygame.time.get_ticks() + self.interval

        while True:
            # if game_area.game_over:
            #     exit()

            current_time = pygame.time.get_ticks()
            self.process_input()
            self.update(game_area)

            if current_time > threshold:
                render.render()
                threshold += self.interval

    def update(self, game_area: GameArea):
        while len(self.__snake_command_buf) != 0:
            game_area.add_snake_turn_command(self.__snake_command_buf.pop(0))

        game_area.update_area_and_check()

    def process_input(self) -> None:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                snake_command = None
                match event.key:
                    case pygame.K_UP:
                        snake_command = Snake.DIRECTION_UP
                    case pygame.K_DOWN:
                        snake_command = Snake.DIRECTION_DOWN
                    case pygame.K_LEFT:
                        snake_command = Snake.DIRECTION_LEFT
                    case pygame.K_RIGHT:
                        snake_command = Snake.DIRECTION_RIGHT
                if snake_command is not None:
                    self.__snake_command_buf.append(snake_command)
