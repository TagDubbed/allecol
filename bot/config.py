from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", "15118169"))
    API_HASH = env.get("TELEGRAM_API_HASH", "678fbf3b58485ef78caf444223045a58")
    OWNER_ID = int(env.get("OWNER_ID", "6784769133"))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "6784769133" "6189141341" "6817045662" ).split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "filetolink_smt_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7025955774:AAFPEu4lAnCcgCfjl20mL7HysL4NS9J__f8")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", "-1002079207446"))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://madflix05-2b0cf1fa2261.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
