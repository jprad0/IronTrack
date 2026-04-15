from fastapi import FastAPI
from database import conn, cursor, criar_tabela
from models import UsuarioCreate,Treino, UsuarioLogin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera tudo (pra desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





criar_tabela()

@app.get("/")
def home():
    return {"msg": "API funcionando"}

@app.get("/debug")
def debug():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

@app.post("/registro")
def registro(usuario: UsuarioCreate):
    cursor.execute(
        "INSERT INTO usuarios (nome, senha) VALUES (?, ?)",
        (usuario.nome, usuario.senha)
    )
    conn.commit()  # ⚠️ ESSENCIAL

    return {"msg": "Usuário criado!"}

@app.post("/login")
def login(usuario: UsuarioLogin):
    nome = usuario.nome.strip()
    senha = usuario.senha.strip()

    print("DEBUG:", nome, senha)  # 👀 vê no terminal

    cursor.execute(
        "SELECT * FROM usuarios WHERE nome=? AND senha=?",
        (nome, senha)
    )

    user = cursor.fetchone()

    if user:
        return {"msg": "Login OK", "user_id": user[0]}
    else:
        return {"msg": "Usuário ou senha inválidos"}


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