from fastapi import FastAPI
from database import conn, cursor, criar_tabela,inserir_exercicios
from models import UsuarioCreate, UsuarioLogin
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

inserir_exercicios()

criar_tabela()

# ==========================
# HOME
# ==========================
@app.get("/")
def home():
    return {"msg": "API funcionando"}

# ==========================
# DEBUG
# ==========================
@app.get("/debug")
def debug():
    cursor.execute("SELECT * FROM usuarios_novo")
    return cursor.fetchall()

# ==========================
# REGISTRO
# ==========================
@app.post("/registro")
def registro(usuario: UsuarioCreate):
    cursor.execute(
        "INSERT INTO usuarios_novo (username, email, senha) VALUES (?, ?, ?)",
        (usuario.username, usuario.email, usuario.senha)
    )
    conn.commit()
    return {"msg": "Usuário criado!"}

# ==========================
# LOGIN
# ==========================
@app.post("/login")
def login(usuario: UsuarioLogin):
    cursor.execute(
        "SELECT * FROM usuarios_novo WHERE username=? AND senha=? AND email=?",
        (usuario.username.strip(), usuario.senha.strip(), usuario.email)
    )

    user = cursor.fetchone()

    if user:
        return {"msg": "Login OK", "user_id": user[0]}
    else:
        return {"msg": "Usuário ou senha inválidos"}

# ==========================
# CALCULAR 1RM
# ==========================
@app.get("/calcular")
def calcular(peso: float, reps: int):
    rm = peso * (1 + reps / 30)
    return {"1rm": round(rm, 2)}

# ==========================
# EXERCICIOS (NOVO)
# ==========================
@app.get("/exercicios")
def listar_exercicios():
    cursor.execute("SELECT * FROM exercicios")
    dados = cursor.fetchall()

    return [{"id": d[0], "nome": d[1], "grupo_muscular": d[2], "equipamento": d[3]} for d in dados]

# ==========================
# ADICIONAR EXERCICIO AO TREINO
# ==========================
@app.post("/treino_exercicios")
def adicionar_exercicio(dados: dict):
    data = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO treino_exercicios 
        (treino_id, exercicio_id, series, repeticoes, peso)
        VALUES (?, ?, ?, ?, ?)
    """, (
        dados["treino_id"],
        dados["exercicio_id"],
        dados["series"],
        dados["repeticoes"],
        dados["peso"]
    ))

    conn.commit()
    return {"msg": "Exercício adicionado ao treino!"}

# ==========================
# LISTAR TREINOS (COM JOIN)
# ==========================
@app.get("/treinos")
def listar_treinos():
    cursor.execute("""
        SELECT 
            te.id,
            e.nome,
            te.peso,
            te.repeticoes,
            t.nome
        FROM treino_exercicios te
        JOIN exercicios e ON te.exercicio_id = e.id
        JOIN treinos t ON te.treino_id = t.id
    """)

    dados = cursor.fetchall()

    resultado = []
    for linha in dados:
        resultado.append({
            "id": linha[0],
            "exercicio": linha[1],
            "peso": linha[2],
            "reps": linha[3],
            "treino": linha[4]
        })

    return resultado