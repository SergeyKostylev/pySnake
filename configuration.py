from exceptions.exceptions import ConfigValueException


SCREEN_SIZE = (500, 500)
SNAKE_FIELD_SIZE = (300, 300)

FIELD_POINT_SIZE = 10

SNAKE_COLOR = (255, 17, 80)
SNAKE_FIELD_COLOR = (0, 102, 102)
TARGET_COLOR = (200, 102, 102)
SCREEN_BACKGROUND_COLOR = (0, 0, 0)

FPS = 60

KEY_UP = 'UP'
KEY_DOWN = 'DOWN'
KEY_LEFT = 'LEFT'
KEY_RIGHT = 'RIGHT'


def validate_configuration() -> None:
    screen_size = SCREEN_SIZE
    snake_field_size = SNAKE_FIELD_SIZE
    if screen_size[0] <= snake_field_size[0]:
        raise ConfigValueException("Screen width must be greater than snake field width.")
    if screen_size[1] <= snake_field_size[1]:
        raise ConfigValueException("Screen height must be greater than snake field height.")

    sizes = {
        "Snake field width": snake_field_size[0],
        "Snake field height": snake_field_size[1],
    }
    for param, value in sizes.items():
        if value % FIELD_POINT_SIZE != 0:
            raise ConfigValueException(f"Invalid '{param}' value '{value}'.")
