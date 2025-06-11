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
    produtos = cursor.fetchall()
    conn.close()

    print("\n Produtos em estoque:")
    for p in produtos:
        print(f"ID: {p[0]}, Nome: {p[1]}, Quantidade: {p[2]} | Preco: R$ {p[3]:.2f}")
    print()

def buscar_produto():
    nome = input("Digite o nome do produto a buscar: ").strip()
    conn = conectar()
    cursor = conn.cursor()