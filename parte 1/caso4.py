vendas = []
total = 0 
m_caro = 0 
m_bararo = 0 
prod_Mcaro = ''
prod_Mbarato = ''
prod_procurado = input("qual o nome do produto que você deseja? \n - ")
encontrado = False

while True:
    nome = input("nome do produto (ou 'sair' para encerrar): \n - ")

    if nome.lower() == "sair": 
        break
    try:
        preco = float(input("preço do produto: \n - "))
    except ValueError: 
        print("preço inválido, tente novamente.")
        continue

    vendas.append((nome, preco))
    total += preco

    if preco > m_caro:
        m_caro = preco
        prod_Mbarato = nome

    if nome.lower() == prod_procurado.lower():
        encontrado = True

    if encontrado: 
        print(f"o produto '{prod_procurado}' foi vendido")

    else: 
        print(f"o produto '{prod_procurado}' não foi vendido")