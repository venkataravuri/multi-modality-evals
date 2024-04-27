import logging
import logging.config

# Declares handlers, formatters and all functions
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'consoleFormatter': {
            'format': '%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
            'datefmt': "%Y-%m-%d:%H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'consoleFormatter'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
})

# Define logger
logger = logging.getLogger("multi-modality-evals")