produto = {}

while True:
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preço do produto:"))
    estoque = int(input("digite a quantidade em estoque:"))
    produto[nome] = [preco, estoque]
    
    continuar = input ("deseja continuar? (sim/não)")
    
    if continuar.lower() == "não":
        break

for chave, valor in produto.items():
    print(chave, valor)