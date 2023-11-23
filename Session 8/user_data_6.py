from pydantic import BaseModel, EmailStr, SecretStr, Field

data = {
    "name":"Hossein",
    "age": "5",
    "email":"hossein@example.com",
    "password":"12345"
}


class UserData(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    email: EmailStr | None = Field(None, alias="EMAIL")
    password: SecretStr


if __name__=="__main__":
    try:
        validated_data = UserData(**data)
        print(f"User Data: {validated_data.model_dump(by_alias=True)}")
    
    except ValueError as err:
        print(f"Error: {err}")