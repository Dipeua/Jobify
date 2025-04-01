from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hashing:
    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password):
        return pwd_context.hash(password)