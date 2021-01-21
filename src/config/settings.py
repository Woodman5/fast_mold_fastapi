import os


DEV = bool(os.environ.get('DEV', True))

if DEV:
    from dotenv import load_dotenv
    load_dotenv()


PROJECT_NAME = "FastMold"
VERSION = "0.1.0"
DESCRIPTION = "Materials DB and process engineering"
SERVER_HOST = os.environ.get("SERVER_HOST", 'localhost')

DEBUG = os.environ.get('DEBUG', False)

# Secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# Rounds for pbkdf2 sha256 password hashing
HASH_ROUNDS = os.environ.get('HASH_ROUNDS', 200000)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = os.environ.get('API_V1_STR', "/api/v1")

# Token 60 minutes * 24 hours * 7 days = 7 days
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 60 * 24 * 7)

# CORS
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:9000",
]

DATABASE_URI = f'postgres://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:5432/' \
               f'{os.environ.get("POSTGRES_DB")}'

USERS_OPEN_REGISTRATION = os.environ.get('USERS_OPEN_REGISTRATION', True)

EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = os.environ.get("EMAIL_RESET_TOKEN_EXPIRE_HOURS", 24)
EMAIL_TEMPLATES_DIR = "src/templates/email-templates/build"

# Email
SMTP_TLS = os.environ.get("SMTP_TLS")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
EMAILS_FROM_EMAIL = os.environ.get("EMAILS_FROM_EMAIL")

EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL
EMAIL_TEST_USER = "yurywoodman@gmail.com"

APPS_MODELS = [
    "src.app.user.models",
    "src.app.auth.models",
    "aerich.models",
]
