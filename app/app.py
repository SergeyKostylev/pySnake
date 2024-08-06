import sys
import pygame
from app import configuration as conf
from app.models.rendered.game_over_window import GameOverWindow
from app.tools.render import Render
from app.models.game_area import GameArea
from app.models.rendered.snake import Snake
from app.models.rendered.info_bar import InfoBar
from app.tools.game_area_builder import build_game_area, build_info_bar


class App:
    interval = 1000 // conf.FPS

    def __init__(self):
        self.__snake_command_buf: list = None
        self.__game_area: GameArea = None
        self.__info_bar: InfoBar = None

        screen = pygame.Surface = pygame.display.set_mode(conf.SCREEN_SIZE)
        self.__render = Render(screen)

    def run(self):
        conf.validate_configuration()
        pygame.init()
        self.__reinit_properties()

        threshold = pygame.time.get_ticks() + self.interval

        while True:
            if self.__game_area.game_over:
                self.__game_over_behavior()

            current_time = pygame.time.get_ticks()

            self.process_input()
            self.update()

            if current_time > threshold:
                self.__render.fill_background()
                self.__render.render(*self.__game_area.get_all_entities())
                self.__render.render(self.__info_bar)
                self.__render.flip_display()

                threshold += self.interval

    def update(self):
        while len(self.__snake_command_buf) != 0:
            self.__game_area.add_snake_turn_command(self.__snake_command_buf.pop(0))

        self.__game_area.update_area()

        stata = self.__game_area.statistics
        self.__info_bar.set_target_amount(stata.achieved_target_count)
        self.__info_bar.set_speed(stata.speed)

    def process_input(self) -> None:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.exit()

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

    def __reinit_properties(self):
        self.__snake_command_buf = []
        self.__game_area: GameArea = build_game_area()
        self.__info_bar = build_info_bar()

    def __game_over_behavior(self):
        game_over_window = GameOverWindow()
        self.__render.render(game_over_window)
        self.__render.flip_display()

        if game_over_window.start_new_game():
            self.__reinit_properties()
        else:
            self.exit()

    def exit(self):
        pygame.quit()
        sys.exit()
