import sqlite3

conn = sqlite3.connect("treinos.db", check_same_thread=False)
cursor = conn.cursor()



def criar_tabela():

    cursor.execute("""
   
    """)

   
    
    

 
def visualizar_tabela():
    cursor.execute("SELECT * FROM treinos")
    print(cursor.fetchall())


    

    
conn.commit()