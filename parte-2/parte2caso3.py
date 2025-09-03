def mercado():
    produtos = [
        ['sorvete', 20, 15.99], 
        ['café', 4, 20.00],
        ['macarrão', 18, 5.99],
        ['açúcar', 20, 4.98],
        ['sal', 2, 3.98],
        ['arroz', 50, 10.99],
        ['leite', 30, 17.00],
        ['pão de forma', 20, 7.99],
        ['margarina', 13, 19.99],
        ['danone', 3, 8.99]
    ]

    
    valor_totalestq = sum(qtd * preco for nome, qtd, preco in produtos)
    print(f"valor total em estoque: R$ {valor_totalestq:.2f} ")
    
    produtomaisvalor = max(produtos, key=lambda item: item[1] * item[2])
    nomevalormaior, qtdmaisvalioso, precomaiscaro = produtomaisvalor
    maiorvalor = qtdmaisvalioso * precomaiscaro  

    print(f"produto de maior valor total: {nomevalormaior} - R$ {maiorvalor:.2f} ")
    
    produtos_estoque_baixo = [nome for nome, qtd, preco in produtos if qtd < 5]
    print("produtos com estoque abaixo de 5 unidades:", produtos_estoque_baixo)
    
    nome_busca = input("digite o nome do produto para a busca: ")    
    produto_encontrado = next((item for item in produtos if item[0].lower() == nome_busca.lower()), None)
    if produto_encontrado:
        nome, qtd, preco = produto_encontrado
        print(f"nome do produto: {nome} - quantidade: {qtd} - preço unitário: R$ {preco:.2f} ")

    else:
        print('produto não encontrado.')
        
mercado()