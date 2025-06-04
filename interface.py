import tkinter as tk
from tkinter import messagebox
from estoque import carregar_estoque, salvar_estoque

class EstoqueApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Estoque")
        self.master.geometry("600x400")
         
        self.estoque = carregar_estoque()

        self.criar_widgets()
        self.exibir_estoque()

    def criar_widgets(self):
        # Labels e entradas
        self.nome_label = tk.Label(self.master, text="Nome do produto:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self.master)
        self.nome_entry.pack()

        self.quantidade_label = tk.Label(self.master, text="Quantidade:")
        self.quantidade_label.pack()
        self.quantidade_entry = tk.Entry(self.master)
        self.quantidade_entry.pack()

        self.preco_label = tk.Label(self.master, text="Preço (R$):")
        self.preco_label.pack()
        self.preco_entry = tk.Entry(self.master)
        self.preco_entry.pack()

        # Botões
        self.adicionar_btn = tk.Button(self.master, text="Adicionar", command=self.adicionar_produto)
        self.adicionar_btn.pack(pady=5)

        self.atualizar_btn = tk.Button(self.master, text="Atualizar", command=self.atualizar_produto)
        self.atualizar_btn.pack(pady=5)

        self.deletar_btn = tk.Button(self.master, text="Deletar", command=self.deletar_produto)
        self.deletar_btn.pack(pady=5)

        self.buscar_btn = tk.Button(self.master, text="Buscar", command=self.buscar_produto)
        self.buscar_btn.pack(pady=5)

        # Lista de produtos
        self.lista = tk.Listbox(self.master, width=70)
        self.lista.pack(pady=10)

    def exibir_estoque(self, produtos=None):
        self.lista.delete(0, tk.END)
        produtos = produtos if produtos is not None else self.estoque
        for produto in produtos:
            texto = f"{produto['nome'].title()} - Quantidade: {produto['quantidade']} - Preço: R$ {produto['preço']:.2f}"
            self.lista.insert(tk.END, texto)

    def adicionar_produto(self):
        nome = self.nome_entry.get().strip().lower()

        if not nome or not self.quantidade_entry.get() or not self.preco_entry.get():
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        try:
            quantidade = int(self.quantidade_entry.get())
            preco = float(self.preco_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e preço devem ser números válidos.")
            return

        if quantidade <= 0 or preco <= 0:
            messagebox.showerror("Erro", "Quantidade e preço devem ser maiores que zero.")
            return

        for produto in self.estoque:
            if produto["nome"] == nome:
                messagebox.showerror("Erro", "Produto já existe no estoque.")
                return

        novo = {
            "nome": nome,
            "quantidade": quantidade,
            "preço": preco
        }

        self.estoque.append(novo)
        salvar_estoque(self.estoque)
        self.exibir_estoque()
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

    def atualizar_produto(self):
        nome = self.nome_entry.get().strip().lower()

        if not nome or not self.quantidade_entry.get() or not self.preco_entry.get():
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        for produto in self.estoque:
            if produto["nome"] == nome:
                try:
                    quantidade = int(self.quantidade_entry.get())
                    preco = float(self.preco_entry.get())
                except ValueError:
                    messagebox.showerror("Erro", "Quantidade e preço devem ser números válidos.")
                    return

                if quantidade <= 0 or preco <= 0:
                    messagebox.showerror("Erro", "Valores inválidos.")
                    return

                produto["quantidade"] = quantidade
                produto["preço"] = preco
                salvar_estoque(self.estoque)
                self.exibir_estoque()
                self.limpar_campos()
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
                return

        messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    def deletar_produto(self):
        nome = self.nome_entry.get().strip().lower()

        for produto in self.estoque:
            if produto["nome"] == nome:
                self.estoque.remove(produto)
                salvar_estoque(self.estoque)
                self.exibir_estoque()
                self.limpar_campos()
                messagebox.showinfo("Sucesso", "Produto deletado com sucesso!")
                return

        messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    def buscar_produto(self):
        termo = self.nome_entry.get().strip().lower()

        resultados = [p for p in self.estoque if termo in p["nome"]]
        if resultados:
            self.exibir_estoque(resultados)
        else:
            messagebox.showinfo("Busca", "Nenhum produto encontrado com esse termo.")

        self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()
