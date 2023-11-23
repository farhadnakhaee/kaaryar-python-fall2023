from pydantic import (
    BaseModel, EmailStr, SecretStr, Field, 
    field_validator
)

data = {
    "name":"Hossein",
    "age": "5",
    "email":"hossein@example.com",
    "password":"123456"
}


class UserData(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    email: EmailStr | None = Field(None, alias="EMAIL")
    password: SecretStr

    def validator1(self):
        self.password
        pass 

    @field_validator('password')
    @classmethod
    def password_validator(cls, value:SecretStr):
        if len(value) < 6:
            raise "Password must contain at least 6 characters"
        return value
    
    @classmethod
    def add(cls, a, b):
        return a+b


if __name__=="__main__":
    try:
        print(UserData.add(1,2))
        validated_data = UserData(**data)
        print(f"User Data: {validated_data.model_dump(by_alias=True)}")
    
    except ValueError as err:
        print(f"Error: {err}")