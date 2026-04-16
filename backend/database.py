import sqlite3

conn = sqlite3.connect("treinos.db", check_same_thread=False)
cursor = conn.cursor()


def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treinos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   exercicio TEXT,
                   peso REAL,
                   reps INTEGER,
                   data TEXT
)
""")    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios_novo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    senha TEXT
)
""")
    
    cursor.execute("""
    drop table if exists usuarios
""")



 
def visualizar_tabela():
    cursor.execute("SELECT * FROM treinos")
    print(cursor.fetchall())

    
conn.commit()