vendas = {}

while True:
    dia = (input("informe o número de vendas do dia/mês (ou 'sair' para encerrar): "))
    if dia.lower() == "sair":
        break
    venda = int(input(f"informe o número de vendas do dia/mês{dia}: "))

    vendas[dia] = {
        "valor": venda,
        }
    
total = sum(dado["valor"] for dado in vendas.values())

mais = max(vendas, key=lambda dia: vendas[dia]["valor"])
menos = min(vendas, key=lambda dia: vendas[dia]["valor"])


print("dias e vendas no mês:")
for dia, dados in vendas.items():

    print(f"dia/Mês: {dia}")
    print(f"vendido: {dados['valor']}")
    print("-" * 30)

print(f"o total de vendas no mês: {total}")
print(f"o dia/mês que mais obteve vendas: {mais}")
print(f"o dia/mês que menos obteve vendas: {menos}")