import logging
from colorlog import ColoredFormatter

# Create a console handler and set the formatter
console_handler = logging.StreamHandler()


logger = logging.getLogger(__name__)
# Add the console handler to the logger
logger.addHandler(console_handler)

formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    
console_handler.setFormatter(formatter)


