import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
        # Frame para entrada de dados
        self.nome_label = tk.Label (self.master, text="Nome do produto:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self.master)
        self.nome_entry.pack()

        self.quantidade_label = tk.Label(self.master, text="Qauntidade:")
        self.quantidade_label.pack()
        self.quantiddade_entry = tk.Entry(self.master)
        self.quantiddade_entry= tk.Entry(self.master)

        self.preco_label = tk.Label(self.master, text="Preço (R$): ")
        self.preco_label.pack()
        self.preco_entry = tk.Entry(self.master)
        self.preco_entry.pack()

        #Botões
        self.adicionar_btn = tk.Button(self.master, text="Adicionar", command=self.adicionar_produto)
        self.adicionar_btn.pack(pady=5)

        
