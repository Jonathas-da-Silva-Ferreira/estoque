import sqlite3

def conectar():
    return sqlite3.connect("estoque.d'")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS produtos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       quantidade integer NOT NULL
                       preco REAL NOT NULL
                   )
                   ''')
    
    conn.commit()
    conn.close()