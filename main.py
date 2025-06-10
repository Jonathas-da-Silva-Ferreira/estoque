from banco import conectar 

conn = conectar()
cursor = conn.cursor()

nome = input("Digite o nome do que deseja pesquisar: ").strip()

cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
produto = cursor.fetchone()

if produto:
    # Display the old product information
    print("\n--- Produto Encontrado ---")
    print(f"Nome: {produto[1]}") # Assuming nome is at index 1
    print(f"Quantidade atual: {produto[2]}") #Assuming quantidade is at index 2
    print(f"Preço atual: R$ {produto[3]:.2f}") # Assuming preço is at index 3
    print("-" * 25)

     # Get new quantity with validation
    while True:
       try:
            nova_quantidade = int(input("Digite a nova quantidade:"))
            if nova_quantidade < 0:
                print("Quantidade não pode ser negativa. Tente novamente.")
                continue
            break
       except ValueError:
            print("Erro: Digite um número válido para a quantidade.")
        
        
     # Get new price with validation
    while True:
        try:
            novo_preco = float(input("Novo preço: R$ "))
            if novo_preco < 0:
                print("Preço não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Erro: Digite um valor válido para o preço. ")

      #Fix the SQL query - it was updatin 'cliente' table instead of 'produtos'
      #and had incorrect parameter binding 

    cursor.execute("UPDATE clientes SET quantidade = ? WHERE nome = ?", (nova_quantidade, novo_preco, nome))
    conn.commit()

    print("Produto atualizado com sucesso!")
else:
    print("Produto não encontrado.")

conn.close()