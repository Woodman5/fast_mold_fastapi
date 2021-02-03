from src.config.settings import APPS_MODELS

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                    "database": "postgres",
                    "host": "127.0.0.1",
                    "password": "postgres",
                    "port": 5432,
                    "user": "postgres",
            }
        }
    },
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        }
    },
}
