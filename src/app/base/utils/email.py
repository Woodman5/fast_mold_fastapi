# from main import logger
import logging
import emails
from emails.template import JinjaTemplate

from src.config.settings import settings

password_reset_jwt_subject = "preset"


def send_email(email_to: str, subject_template="", html_template="", environment={}):
    """Отправка email"""
    assert settings.EMAILS_ENABLED, "no provided configuration for email variables"
    message = emails.html(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(settings.emails_from_name, settings.emails_from_email),
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}

    if settings.smtp_ssl:
        smtp_options["ssl"] = True
    if settings.smtp_user:
        smtp_options["user"] = settings.smtp_user
    if settings.smtp_password:
        smtp_options["password"] = settings.smtp_password
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.debug(f"send email result: {response}")
