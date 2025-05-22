import json
import os

ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, "r") as file:
            return json.load(file)
    else:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, "w") as file:
        json.dump(estoque, file, indent=4)

def buscar_produto(termo_buscar, estoque):
    termo_buscar = termo_buscar.lower()
    resultados = []

    for produto in estoque:
        if termo_buscar in produto["nome"].lower():
            resultados.append(produto)

    return resultados
