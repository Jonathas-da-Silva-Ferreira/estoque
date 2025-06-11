from banco import conectar, criar_tabela

def adicionar_produto(nome, quantidade, preco):
    nome = input("Nome do produto: ").strip()
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço (R$): "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO estoque (nome, quantidade, preco) VALUES (?, ?, ?)",  (nome, quantidade, preco))
    conn.commit()
    conn.close()
    print("Produto adicionado com sucesso!")

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estoque")
    