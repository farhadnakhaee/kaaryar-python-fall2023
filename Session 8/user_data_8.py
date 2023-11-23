from pydantic import (
    BaseModel, EmailStr, SecretStr, Field, 
    model_validator
)

data = {
    # "name":"Hossein",
    "age": "25",
    "email":"hossein@example.com",
    # "password":"123HoSSeIn45"
}


class UserData(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    email: EmailStr | None = Field(None, alias="EMAIL")
    password: SecretStr

    @model_validator(mode="after")
    def password_check(self):
        if self.name.lower() in self.password.get_secret_value().lower():
            raise "Name must not appear in password"
        return self


if __name__=="__main__":
    try:
        validated_data = UserData(**data)
        print(f"User Data: {validated_data.model_dump(by_alias=True)}")
    
    except ValueError as err:
        print(f"Error: {err}")