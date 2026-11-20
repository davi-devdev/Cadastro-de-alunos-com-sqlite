# Cadastro de produtos

# Feito por:
# Davi Lopes (01912493)
# Marcos Davi (01874151)
# Fernando Gabriel (01899997)

import sqlite3

con = sqlite3.connect("database.db") # Atualizar aqui
con.set_trace_callback(print)
cur = con.cursor()

def cadastrar_produto(nome, preco):
    cur.execute(f"INSERT INTO Produtos (nome, preco) VALUES ('{nome}', {preco})")
    
    return con.commit()


def remover_produto(id):
    cur.execute(f"DELETE FROM Produtos WHERE id = {id}")
    
    return con.commit()


def obter_produto(nome = ''):
    produtos = []

    if nome == '':
        select_produtos = cur.execute("SELECT * FROM Produtos")
    
        produtos = select_produtos.fetchall()

    if nome != '':
        select_produtos = cur.execute(f"SELECT * FROM Produtos WHERE nome = '{nome}'")

        produtos = select_produtos.fetchone()


    if produtos is None: return []

    return produtos

def obter_produto_por_id(id):
    select_produto = cur.execute(f"SELECT * FROM PRODUTOS WHERE id = {id}")
    
    return select_produto.fetchone()


def editar_produto(id, nome, preco):
    if obter_produto_por_id(id):
        cur.execute(f"UPDATE Produtos SET nome = '{nome}', preco = {preco} WHERE id = {int(id)}")

    return con.commit() 


def print_produto(produto):
    print(f"ID: {produto[0]}\nNome: {produto[1]}\nPreço: {produto[2]}")


while True:
    print(
        """
        - Menu de opções - 
        1. Adicionar produto
        2. Remover produto
        3. Procurar produto
        4. Editar produto
        5. Sair
        """
    )

    opcao = input("Digite uma opção: ")

    if opcao == '1':
        # Pedindo dados dos produtos
        nome = input("Insira o nome do produto: ")
        preco = input("Insira o preço do produto (formato: 10.2): ")

        print("Cadastrando...")
        cadastrar_produto(nome, preco)

        for produto in obter_produto():
            print(produto)


    if opcao == '2':
        id = int(input("Insira o id do produto a ser removido: "))

        print("Removendo...")
        remover_produto(id)
        print("Removido!")


    if opcao == '3':
        nome = input("Insira o nome do produto a ser pesquisado\n(Vazio para ver tudo): ") 

        resultado = obter_produto(nome)

        if nome == "":
            for i in resultado:
                print_produto(i)
                print('-'*3)
        else:
            print_produto(resultado)

    if opcao == '4':
        id = input("Insira o id do produto: ")

        if obter_produto_por_id(int(id)):
            nome = input("Insira novo nome do produto: ")
            preco = input("Insira o novo preço do produto: ")

            editar_produto(id, nome, preco)

    if opcao == '5':
        print("Saindo...")
        break 
