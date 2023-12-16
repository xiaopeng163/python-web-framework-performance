from fastapi import FastAPI
from pydantic import BaseModel, field_validator


app = FastAPI()

class User(BaseModel):
    name: str
    age: int

    @field_validator('age')
    def check_age(cls, v):
        if v < 0:
            raise ValueError('must be >= 0')
        return v


@app.get('/{greeting}')
def helloworld(greeting):
    return f"{greeting}, world!"


@app.post('/user')
def create_user(user: User):
    return user