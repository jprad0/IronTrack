from fastapi import FastAPI
from database import conn, cursor, criar_tabela
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera tudo (pra desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Treino(BaseModel):
    exercicio: str
    peso: float
    reps: int


criar_tabela()

@app.get("/")
def home():
    return {"msg": "API funcionando"}

@app.get("/calcular")
def calcular(peso: float, reps: int):
    rm = peso * (1 + reps/30)
    return {"Repetição Maxima em kg": rm}


@app.post("/salvar")
def salvar(treino: Treino):
    from datetime import datetime

    data = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
    "INSERT INTO treinos (exercicio, peso, reps, data) VALUES (?, ?, ?, ?)",
    (treino.exercicio, treino.peso, treino.reps, data)
)
    conn.commit()

    return {"msg": "Treino salvo!"}

@app.get("/treinos")
def listar_treinos():
    cursor.execute("SELECT * FROM treinos")
    dados = cursor.fetchall()

    resultado = []
    for linha in dados:
        resultado.append({
            "id": linha[0],
            "exercicio": linha[1],
            "peso": linha[2],
            "reps": linha[3],
            "data": linha[4]
        })

    return resultado