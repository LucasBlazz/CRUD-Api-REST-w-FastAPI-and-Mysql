from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50
    )
    email: EmailStr
    password: str = Field(
        min_length=8
    )