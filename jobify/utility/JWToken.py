from datetime import datetime, timedelta, timezone
from jose import JWSError, jwt

SECRET_KEY = "a74a9ae4210f16ee64b586fa020a223cf2e56e341493ac805a77c88ff46df936"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class JWToken:
    
    @classmethod
    def create_access_token(cls, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt