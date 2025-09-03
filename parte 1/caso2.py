lista = []

def compras(x):
    while True:
        item = input("digite itens para a lista de compras e, logo após digite 'sair' para encerrar:")

        if item.lower() == "sair":
            break
        x.append(item)

    print(sorted(x))

compras(lista)