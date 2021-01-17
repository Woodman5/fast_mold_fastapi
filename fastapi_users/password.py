from typing import Tuple

from passlib import pwd
from passlib.context import CryptContext


HASH_ROUNDS = 200000

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated='auto', pbkdf2_sha256__rounds=HASH_ROUNDS)


def verify_and_update_password(plain_password: str, hashed_password: str) -> Tuple[bool, str]:
    return pwd_context.verify_and_update(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def generate_password() -> str:
    return pwd.genword()
