from app.tools.exceptions import ConfigValueException

SCREEN_SIZE = (600, 400)
SNAKE_FIELD_SIZE = (400, 360)
INFO_BAR_SIZE = (170, 70)
DIALOG_WINDOW_SIZE = (SCREEN_SIZE[0] // 100 * 60, SCREEN_SIZE[1] // 100 * 60)  # 60 is percent

FIELD_POINT_SIZE = 10

SNAKE_START_LENGTH = 3
SNAKE_START_SPEED = 150

INFO_BAR_TEXT_SIZE = 21
DIALOG_WINDOW_TEXT_SIZE = 21

SCREEN_BACKGROUND_COLOR = (0, 0, 0)
SNAKE_FIELD_COLOR = (0, 102, 102)
SNAKE_COLOR = (255, 17, 80)
TARGET_COLOR = (218, 112, 214)
INFO_BAR_COLOR_BORDER = (255, 255, 255)
INFO_BAR_COLOR_TEXT = INFO_BAR_COLOR_BORDER
DIALOG_WINDOW_COLOR = (176, 196, 222)
DIALOG_WINDOW_TEXT_COLOR = (65, 105, 225)

FPS = 60

def validate_configuration() -> None:
    screen_size = SCREEN_SIZE
    snake_field_size = SNAKE_FIELD_SIZE
    info_bar_size = INFO_BAR_SIZE
    if screen_size[0] <= snake_field_size[0]:
        raise ConfigValueException("Screen width must be greater than snake field width.")
    if screen_size[1] <= snake_field_size[1]:
        raise ConfigValueException("Screen height must be greater than snake field height.")

    sizes = {
        "Snake field width": snake_field_size[0],
        "Snake field height": snake_field_size[1],
        "Info bar width": info_bar_size[0],
        "Info bar height": info_bar_size[1],
    }
    for param, value in sizes.items():
        if value % FIELD_POINT_SIZE != 0:
            raise ConfigValueException(f"Invalid '{param}' value '{value}'.")

    if (SNAKE_FIELD_SIZE[0] + info_bar_size[0]) > screen_size[0]:
        raise ConfigValueException("Sum of Snake field and Info bar widths must be less than screen width.")
