import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

def create_admin_token():
    expires_delta = timedelta(hours=1)
    data={"role": "ADMIN"}
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    output = jwt.encode(to_encode, os.getenv("JWT_SECRET_KEY"), algorithm="HS256")
    print("Below is the admin access Token - \n")
    print(output)

create_admin_token()