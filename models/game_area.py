import pygame
import configuration as const
from models.running_game_statistics import RunningGameStatistics
from models.rendered.snake import Snake
from models.rendered.snake_field import SnakeField
from models.rendered.target import Target
import random


class GameArea:
    def __init__(self):
        self.__snake_field = self.__build_snake_field()
        self.__snake = self.__build_snake()
        self.__target = self.recreate_target()
        self.__statistics = RunningGameStatistics()
        self.__game_over = False

    def get_all_entities(self):
        return self.__snake_field, self.__snake, self.__target

    @property
    def snake(self):
        return self.__snake

    @property
    def game_over(self):
        return self.__game_over

    def check_updates(self) -> None:
        head = self.__snake.body[0]

        if head.colliderect(self.__target.body):  # snake head on target position
            self.__statistics.add_eat_target()
            self.__snake.grow()

            self.__snake.speed_coefficient += 0.7
            print(self.__snake.speed_coefficient)

            # TODO: speed up
            self.recreate_target()

        if not head.colliderect(self.__snake_field.field):  # snake outside field
            self.__game_over = True

        if self.__snake.snake_intersection():
            self.__game_over = True

    def recreate_target(self) -> Target:
        ramdom_empy_point = random.choice(self.__get_empy_field_points()) # TODO: if we have not empty points it is a victory
        self.__target = Target(ramdom_empy_point[0], ramdom_empy_point[1])

        return self.__target

    def __build_snake(self) -> Snake:
        snake_field_center_position = self.__snake_field.get_center_point()

        snake_field_center_position = (  # TODO: remove after testing FOR
            snake_field_center_position[0] + 120,
            snake_field_center_position[1]
        )

        return Snake(position=snake_field_center_position)

    def __get_empy_field_points(self):
        snake_field_rect = self.__snake_field.field
        field_x_from = snake_field_rect.x
        field_y_from = snake_field_rect.y
        field_x_to = snake_field_rect.width + field_x_from
        field_y_to = snake_field_rect.height + field_y_from

        filled_filed_points = []
        for piece in self.__snake.body:
            filled_filed_points.append((piece.x, piece.y))

        empty_filed_points = []
        for i in range(field_x_from, field_x_to, const.FIELD_POINT_SIZE):
            for j in range(field_y_from, field_y_to, const.FIELD_POINT_SIZE):
                point = (i, j)
                if point not in filled_filed_points:
                    empty_filed_points.append(point)

        return empty_filed_points

    def __build_snake_field(self) -> SnakeField:
        screen_size = const.SCREEN_SIZE
        field_size = const.SNAKE_FIELD_SIZE
        # x = (screen_size[0] - field_size[0]) // 2
        x = 20  # temporary  solution
        y = (screen_size[1] - field_size[1]) // 2

        return SnakeField(const.SNAKE_FIELD_SIZE[0], const.SNAKE_FIELD_SIZE[1], x, y)
