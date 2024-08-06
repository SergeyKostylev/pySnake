class RunningGameStatistics:

    def __init__(self):
        self.__achieved_target_count = 0
        self.__speed = None

    @property
    def achieved_target_count(self):
        return self.__achieved_target_count

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def add_achieved_target(self):
        self.__achieved_target_count += 1
