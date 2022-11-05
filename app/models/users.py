from pydantic import BaseModel, Field, validator
from fastapi import HTTPException


class User(BaseModel):
    # "COMPOSITION", Data Modeling
    id: str = Field(None, description='Id do usuário.')
    name: str = Field(None, description='Nome do usuário.')
    last_name: str = Field(None, description='Sobrenome do usuário.')
    age: int = Field(None, description='Idade do usuário.')


    @validator('name')
    def must_have_name(cls, name):
        if not name:
            raise HTTPException(status_code=404, detail="Usuário não tem nome!")
        return name.title()