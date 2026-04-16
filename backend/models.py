from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    username: str
    email: str
    senha: str

class Treino(BaseModel):
    exercicio: str
    peso: float
    reps: int

class UsuarioLogin(BaseModel):
    username: str
    email: str
    senha: str