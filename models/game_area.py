from models.running_game_statistics import RunningGameStatistics
from models.rendered.snake import Snake
from models.rendered.snake_field import SnakeField
from models.rendered.target import Target
from services.helpers import get_random_empy_field_point


class GameArea:
    def __init__(self, snake: Snake, snake_field: SnakeField, target: Target):
        self.__snake_field = snake_field
        self.__snake = snake
        self.__target = target
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

            self.edit_target_place()

        if not head.colliderect(self.__snake_field.field):  # snake outside field
            self.__game_over = True

        if self.__snake.snake_intersection():
            self.__game_over = True

    def edit_target_place(self):
        point = get_random_empy_field_point(self.__snake_field, self.__snake) # TODO: if we have not empty points it is a victory
        self.__target.body.x = point[0]
        self.__target.body.y = point[1]
