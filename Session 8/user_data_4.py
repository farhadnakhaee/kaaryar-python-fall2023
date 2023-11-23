# from typing import Optional
from pydantic import BaseModel, EmailStr, SecretStr

data = {
    "name":"Hossein",
    "age": "15",
    # "email":"hossein@example.com",
    "password":"12345"
}


class UserData(BaseModel):
    name: str
    age: int
    email_address: EmailStr | None = None
    password: SecretStr

if __name__=="__main__":
    try:
        validated_data = UserData(**data)
        print(f"User Data: {validated_data.model_dump()}")
    
    except ValueError as err:
        print(f"Error: {err}")