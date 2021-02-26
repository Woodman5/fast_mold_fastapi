from src.app.base.utils.email import send_email
from src.config.settings import settings
from pathlib import Path


def send_test_email(email_to: str):
    """ Отправка тестового письма
    """
    project_name = settings.project_name
    subject = f"{project_name} - Test email"
    with open(Path(settings.email_templates_dir) / "test_email.html") as f:
        template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": settings.project_name, "email": email_to},
    )


def send_reset_password_email(email_to: str, email: str, token: str):
    """ Отправка письма при сбросе пароля
    """
    project_name = settings.project_name
    subject = f"{project_name} - Password recovery for user {email}"
    with open(Path(settings.email_templates_dir) / "reset_password.html") as f:
        template_str = f.read()
    if hasattr(token, "decode"):
        use_token = token.decode()
    else:
        use_token = token
    server_host = settings.server_host
    link = f"{server_host}/reset-password?token={use_token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.project_name,
            "username": email,
            "email": email_to,
            "valid_hours": settings.email_reset_token_expire_hours,
            "link": link,
        },
    )


def send_new_account_email(email_to: str, username: str, password: str, uuid: str):
    """ Отправка письма при создании пользователя
    """
    project_name = settings.project_name
    subject = f"{project_name} - New account for user {username}"
    with open(Path(settings.email_templates_dir) / "new_account.html") as f:
        template_str = f.read()
    link = f"{settings.server_host}/{settings.api_v1_str}/confirm-email?link={uuid}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.project_name,
            "username": username,
            "password": password,
            "email": email_to,
            "link": link,
        },
    )
