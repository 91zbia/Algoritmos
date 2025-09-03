agenda = {}

while True:
    nome = input("digite para quem deseja ligar: ")
    telefone = input("digite o número de telefone: ")

    agenda[nome] = telefone 

    continuar = input("deseja adicionar outro contato? (sim/não)")

    if continuar.lower() == "não":
        break

print("\n")
for chave, valor in agenda.items():
    print(chave, valor)

