import jwt
from datetime import datetime, timedelta
from flask import current_app

def create_access_token(data, expires_delta=timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, current_app.config["JWT_SECRET_KEY"], algorithm="HS256")

def decode_access_token(token):
    try:
        payload = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
