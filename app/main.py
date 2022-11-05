import json
from pathlib import Path
from typing import List
from app.models.users import User
import uvicorn
from fastapi import FastAPI, Response, status



app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / 'app/internal/database.json'


@app.get('/users')
async def read_users(response: Response) -> List[User]:
    """ Read Users: Essa função lê todos os usuários do banco de dados. """

    with open(file_path) as file:
        archive = json.loads(file.read())
        response.status_code = status.HTTP_202_ACCEPTED
    return archive


@app.get('/users/{_id}')
async def read_user_by_id(_id: int, response: Response) -> User or dict:
    """ Read User By ID: Essa função lê usuários do banco de dados pelo seu id. """

    with open(file_path) as file:  # criando um 'context', para jogar o arquivo dentro de uma variável
        archive = json.loads(file.read())  # lendo o arquivo do banco de dados que foi colocado na variável file
        users = archive[1].get('results')  # pegando o primeiro elemento da lista do banco de dados '[{}]->{}'(dict)
        for user in users:
            if user.get('id') == _id:
                return User(**user)
        return {'msg': f'Usuário {_id} não existe!'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=8000, reload=True)