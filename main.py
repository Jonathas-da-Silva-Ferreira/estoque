from estoque import carregar_estoque, salvar_estoque, buscar_produto
from tabulate import tabulate

def menu():
    print("\nEscolha uma opção:")
    print("1 - Ver estoque")
    print("2 - Cadastrar produto")
    print("3 - Deletar produto")
    print("4 - Sair")
    print("5 - Atualizar produto")
    print("6 - Buscar produto")
    print("7 - Relatorio de estoque")

estoque = carregar_estoque()

while True:
    menu()
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        if len(estoque) == 0:
            print("Estoque vazio.")
        else:
            tabela = [[p['nome'], p["quantidade"], f"R${p['preço']:.2f}"] for p in estoque]
            print("\nItens no Estoque:")
            print(tabulate(tabela, headers=["Produto", "Quantidade", "Preço (R$)"], tablefmt="grid"))

    elif opcao == "2":
        nome = input("Digite o nome do produto: ").lower()
        if any(p['nome'].lower() == nome for p in estoque):
            print(f"Produto '{nome}' já cadastrado no sistema.")
        else:
            try:
                quantidade = int(input("Digite a quantidade: "))
                preco = float(input("Digite o preço (R$): "))

                if quantidade <= 0:
                    print("Erro: A quantidade deve ser positiva.")
                elif preco <= 0:
                    print("Erro: O preço deve ser positivo.")
                else:
                    estoque.append({"nome": nome, "quantidade": quantidade, "preço": preco})
                    salvar_estoque(estoque)
                    print(f"Produto '{nome}' cadastrado com sucesso!")
            except ValueError:
                print("Erro: Entrada inválida. Use números para quantidade e preço.")

    elif opcao == "3":
        nome = input("Digite o nome do produto que deseja deletar: ").lower()
        for produto in estoque:
            if produto['nome'].lower() == nome:
                estoque.remove(produto)
                salvar_estoque(estoque)
                print(f"Produto '{nome}' deletado com sucesso!")
                break
        else:
            print(f"Produto '{nome}' não encontrado.")

    elif opcao == "4":
        salvar_estoque(estoque)
        print("Saindo do programa...")
        break

    elif opcao == "5":
        nome = input("Digite o nome do produto que deseja atualizar: ").lower()
        for produto in estoque:
            if produto["nome"].lower() == nome:
                try:
                    nova_qtd = int(input("Digite a nova quantidade: "))
                    novo_preco = float(input("Digite o novo preço (R$): "))
                    if nova_qtd <= 0:
                        print("Erro: Quantidade deve ser positiva.")
                    elif novo_preco <= 0:
                        print("Erro: Preço deve ser positivo.")
                    else:
                        produto["quantidade"] = nova_qtd
                        produto["preço"] = novo_preco
                        salvar_estoque(estoque)
                        print(f"Produto '{nome}' atualizado com sucesso!")
                except ValueError:
                    print("Erro: Entrada inválida. Use números para quantidade e preço.")
                break
        else:
            print(f"Produto '{nome}' não encontrado.")

    elif opcao == "6":
        termo_buscar = input("Digite o nome ou parte do nome do produto: ")
        resultados = buscar_produto(termo_buscar, estoque)
        if resultados:
           tabela = [[p["nome"], p["quantidade"], f'R${p["preço"]:.2f}'] for p in resultados]
           print(f"\nResultados da busca por {termo_buscar}:")
           print(tabulate(tabela, headers=["Produto", "Quantidade", "Preço (R$)"], tablefmt="grid"))
           print(f"Total de produtos encontrados: {len(resultados)}")

        else:
            print(f"Nenhum produto encontrado com o termo '{termo_buscar}'.")


    elif opcao == "7":
        if len(estoque) == 0:
            print("Estoque vazio.")
        else:
            total_itens = sum(p["quantidade"] for p in estoque)
            valor_total = sum(p['quantidade'] * p['preço'] for p in estoque)
            print("\nRelatório de Estoque:")
            print(f"Total de itens diferentes: {len(estoque)}")
            print(f"Total de itens (somando quantidades): {total_itens}")
            print(f"Valor total do estoque: R${valor_total:.2f}")

    else:
        print("Opção inválida. Tente novamente.")

    print(f"Total de itens no estoque: {len(estoque)}")
