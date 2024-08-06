import pygame

from app.models.game_area_state import GameAreaState
from app.models.running_game_statistics import RunningGameStatistics
from app.models.rendered.snake import Snake
from app.models.rendered.snake_field import SnakeField
from app.models.rendered.target import Target
from app.tools.helpers import get_random_empy_field_point


class GameArea:
    def __init__(self, snake: Snake, snake_field: SnakeField, target: Target):
        self.__snake_field = snake_field
        self.__snake = snake
        self.__target = target
        self.__statistics = RunningGameStatistics()
        self.__game_over = False
        self.__snake_turn_commands_queue = []
        self.__state = GameAreaState()

    @property
    def snake(self):
        return self.__snake

    @property
    def game_over(self):
        return self.__game_over

    @property
    def statistics(self) -> RunningGameStatistics:
        speed_value = self.__snake.speed
        self.__statistics.speed = int((1000 - speed_value) / 10)
        return self.__statistics

    def get_all_entities(self):
        return self.__snake_field, self.__snake, self.__target

    def add_snake_turn_command(self, snake_command):
        self.__snake_turn_commands_queue.append(snake_command)

    def update_area(self) -> None:
        while len(self.__snake_turn_commands_queue) != 0:
            self.__snake.set_direction(self.__snake_turn_commands_queue.pop(0))

        if (pygame.time.get_ticks() > self.__state.last_snake_moving_time + self.__snake.speed):
            self.__state.update_last_snake_moving_time()
            self.__snake.do_step()

        head = self.__snake.body[0]

        if head.colliderect(self.__target.body):  # snake head on target position
            self.__statistics.add_achieved_target()
            self.__snake.grow()
            self.__snake.speed_up()

            self.edit_target_place()

        if not head.colliderect(self.__snake_field.field):  # snake outside field
            self.__game_over = True

        if self.__snake.snake_intersection():
            self.__game_over = True

    def edit_target_place(self):
        point = get_random_empy_field_point(self.__snake_field, self.__snake)
        # TODO: if we have not empty points it is a victory
        self.__target.body.x = point[0]
        self.__target.body.y = point[1]
