import tkinter as tk
from tkinter import ttk, messagebox

# Lista de produtos
produtos = []

def cadastrar_produto():
    def salvar_produto():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        try:
            valor = float(entry_valor.get())
        except ValueError:
            messagebox.showerror("Erro", "O valor do produto deve ser um número válido.")
            return
        disponivel = var_disponivel.get()

        if not nome or not descricao or not entry_valor.get():
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        produtos.append({"nome": nome, "descricao": descricao, "valor": valor, "disponivel": disponivel})
        atualizar_listagem()
        janela_cadastro.destroy()

    # Janela de cadastro
    janela_cadastro = tk.Toplevel(root)
    janela_cadastro.title("Cadastrar Produto")

    tk.Label(janela_cadastro, text="Nome do Produto:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(janela_cadastro, text="Descrição do Produto:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entry_descricao = tk.Entry(janela_cadastro)
    entry_descricao.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela_cadastro, text="Valor do Produto:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entry_valor = tk.Entry(janela_cadastro)
    entry_valor.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(janela_cadastro, text="Disponível para Venda:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    var_disponivel = tk.StringVar(value="sim")
    tk.Radiobutton(janela_cadastro, text="Sim", variable=var_disponivel, value="sim").grid(row=3, column=1, sticky="w", padx=10, pady=5)
    tk.Radiobutton(janela_cadastro, text="Não", variable=var_disponivel, value="não").grid(row=3, column=1, sticky="e", padx=10, pady=5)

    tk.Button(janela_cadastro, text="Salvar", command=salvar_produto).grid(row=4, column=0, columnspan=2, pady=10)

def atualizar_listagem():
    for item in tree.get_children():
        tree.delete(item)

    produtos_ordenados = sorted(produtos, key=lambda x: x["valor"])
    for produto in produtos_ordenados:
        tree.insert("", "end", values=(produto["nome"], f"R$ {produto['valor']:.2f}"))

# Janela principal
root = tk.Tk()
root.title("Cadastro e Listagem de Produtos")

# Frame para a listagem
frame_listagem = tk.Frame(root)
frame_listagem.pack(padx=10, pady=10, fill="both", expand=True)

tree = ttk.Treeview(frame_listagem, columns=("nome", "valor"), show="headings")
tree.heading("nome", text="Nome")
tree.heading("valor", text="Valor")
tree.column("nome", width=200)
tree.column("valor", width=100)

tree.pack(fill="both", expand=True)

# Botão para cadastrar novo produto
tk.Button(root, text="Cadastrar Novo Produto", command=cadastrar_produto).pack(pady=10)

root.mainloop()
