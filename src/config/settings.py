import os
from pydantic import BaseSettings, PostgresDsn, Field


class Settings(BaseSettings):

    dev: bool = True

    project_name: str = "FastMold"
    version: str = "0.1.0"
    description: str = "Materials DB and process engineering"

    server_host: str = 'localhost'
    server_port: int = 8000

    api_v1_str: str = "/api/v1"

    debug: bool = False

    # Documentation
    hide_docs: bool = False
    openapi_url: str = "/openapi.json"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"

    # Secret key
    secret_key: str = 'je+5gyn7w4hqfb_gtf=e)@t!0s(K+_+69@sg%6f+u(dtvs0u9u'

    # Session cookie name
    session_cookie_name: str = 'Session'

    # Rounds for pbkdf2 sha256 password hashing
    hash_rounds: int = 200000

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Token 60 minutes * 24 hours * 7 days = 7 days
    access_token_expire_minutes: int = 60 * 24 * 7

    # CORS
    backend_cors_origins: list = [
        "http://localhost",
        "http://localhost:4200",
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:9000",
    ]

    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str

    users_open_registration: bool = True

    # Email
    emails_from_name: str = project_name
    email_reset_token_expire_hours: int = 24
    email_templates_dir: str = "src/templates/email-templates/ready"
    smtp_ssl: bool
    smtp_port: int
    smtp_host: str
    smtp_user: str
    smtp_password: str
    emails_from_email: str

    emails_enabled: bool = False
    email_test_user: str = "youriywoodman@gmail.com"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def database_uri(self):
        return f'postgresql://{self.postgres_user}:' \
               f'{self.postgres_password}@' \
               f'{self.postgres_host}:5432/' \
               f'{self.postgres_db}'


settings = Settings()
