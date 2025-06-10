from banco import conectar 

conn = conectar()
cursor = conn.cursor()

nome = input("Digite o nome do que deseja pesquisar: ").strip()

cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
produto = cursor.fetchone()

if produto:
    nova_quantidade = int(input("Digite a nova quantidade:"))
    novo_preco = float(input("Novo preço: "))

    cursor.execute("UPDATE clientes SET quantidade = ? WHERE nome = ?", (nova_quantidade, novo_preco, nome))
    conn.commit()

    print("Produto atualizado com sucesso!")
else:
    print("Produto não encontrado.")

conn.close()