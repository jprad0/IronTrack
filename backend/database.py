import sqlite3

conn = sqlite3.connect("treinos.db", check_same_thread=False)
cursor = conn.cursor()



def criar_tabela():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios_novo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        senha TEXT
)
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        nome TEXT, -- Ex: Treino A, Peito e Triceps
        FOREIGN KEY (usuario_id) REFERENCES usuarios_novo(id)
)
""")    
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        grupo_muscular TEXT,
        equipamento TEXT
                   
)
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treino_exercicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        treino_id INTEGER,
        exercicio_id INTEGER,
        series INTEGER,
        repeticoes INTEGER,
        peso REAL,
        FOREIGN KEY (treino_id) REFERENCES treinos(id),
        FOREIGN KEY (exercicio_id) REFERENCES exercicios(id)
)
""")
    
    

 
def visualizar_tabela():
    cursor.execute("SELECT * FROM treinos")
    print(cursor.fetchall())

def inserir_exercicios():
    exercicios = [
        ("Supino Reto", "Peito", "Barra ou Halteres"),
        ("Supino Inclinado", "Peito", "Barra ou Halteres"),
        ("Cross Over", "Peito", "Polias")  
    ]
    
    cursor.executemany("""
    INSERT INTO exercicios (nome, grupo_muscular, equipamento) 
    VALUES (?, ?, ?)
    """, exercicios)
    
conn.commit()