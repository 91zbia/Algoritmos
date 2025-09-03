def loja():
    vendas = []
    for i in range(1, 31):
        venda = int(input(f"informe o número de vendas do dia {i}: \n -"))
        vendas.append(venda)

    totalvendas = sum(vendas)
    diamaisvendas = vendas.index(max(vendas)) + 1
    diamenosvendas = vendas.index(min(vendas)) + 1
    mediavendas = totalvendas / len(vendas)
    diasacimamedia = [i + 1 for i, v in enumerate(vendas) if v > mediavendas]

    print(f"o total de vendas no mês: {totalvendas}")
    print(f"o dia com mais vendas: {diamaisvendas} (vendas: {max(vendas)})")
    print(f"o dia com menos vendas: {diamenosvendas} (vendas: {min(vendas)})")
    print(f"a média de vendas por dia: {mediavendas:.2f}")
    print(f"os dias com as vendas acima da média: {diasacimamedia}")
    
loja()