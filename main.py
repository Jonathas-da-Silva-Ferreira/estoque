from banco import conectar 

conn = conectar()
cursor = conn.cursor()

nome = input("Digite o nome do produto que deseja atualizar: ").strip()

cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
produto = cursor.fetchone()

if produto:
    print("\n--- Produto Encontrado ---")
    print(f"Nome: {produto[1]}")
    print(f"Quantidade atual: {produto[2]}")
    print(f"Preço atual: R$ {produto[3]:.2f}")
    print("-" * 25)

    # Validação de quantidade
    while True:
        try:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            if nova_quantidade < 0:
                print("Quantidade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número válido para a quantidade.")

    # Validação de preço
    while True:
        try:
            novo_preco = float(input("Novo preço: R$ "))
            if novo_preco < 0:
                print("Preço não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Erro: Digite um valor válido para o preço.")

    # Atualização no banco de dados
    cursor.execute(
        "UPDATE produtos SET quantidade = ?, preco = ? WHERE nome = ?",
        (nova_quantidade, novo_preco, nome)
    )
    conn.commit()
    print("✅ Produto atualizado com sucesso!")
else:
    print("❌ Produto não encontrado.")

conn.close()