# https://docs.pydantic.dev/latest/why/

from pydantic import BaseModel, EmailStr, SecretStr

data = {
    "name":"Hossein",
    "age": "15",
    "email":"hossein@example.com",
    "password":"12345"
}

class UserData(BaseModel):
    name: str
    age: int
    email: EmailStr
    password: SecretStr

class UserDataOut(BaseModel):
    name: str
    age: int


def print_my_data(mydata: UserData):
    output_data = UserDataOut.model_validate(mydata, from_attributes=True)
    print(f"User Data: {output_data.model_dump()}")


if __name__=="__main__":
    try:
        validated_data = UserData(**data)
        print_my_data(validated_data)
    
    except ValueError as err:
        print(f"Error: {err}")