from banco import criar_tabela, conectar

#criar_tabela()
criar_tabela()

#Adcionar produtos
conn = conectar()
cursor = conn.cursor()

produtos = [
    ("Arroz", 10, 5.99),
    ("Feijão", 20, 4.49),
    ("Macarrão", 15, 2.99)
    ]

cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)", produtos)

conn.commit()


#Exibir produtos
cursor.execute("SELECT * FROM produtos")
todos = cursor.fetchall()

for produto in todos:
    print(f"ID: {produtos[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: R$ {produto[3]:.2f}")

conn.close()