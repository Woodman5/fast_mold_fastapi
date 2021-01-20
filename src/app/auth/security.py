from typing import Tuple

from passlib.context import CryptContext
from passlib import pwd

from src.config.settings import HASH_ROUNDS


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated='auto', pbkdf2_sha256__rounds=HASH_ROUNDS)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def verify_and_update_password(plain_password: str, hashed_password: str) -> Tuple[bool, str]:
    return pwd_context.verify_and_update(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def generate_password() -> str:
    return pwd.genword()
