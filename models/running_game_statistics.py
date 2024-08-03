from collections import Counter


class RunningGameStatistics:

    def __init__(self):
        self.__achieved_target_count = 0

    @property
    def target_eat_count(self):
        return self.__achieved_target_count

    def add_eat_target(self):
        self.__achieved_target_count += 1