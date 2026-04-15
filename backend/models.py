from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    senha: str

class Treino(BaseModel):
    exercicio: str
    peso: float
    reps: int

class UsuarioLogin(BaseModel):
    nome: str
    senha: str