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
    
def visualizar_tabela():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
    
conn.commit()