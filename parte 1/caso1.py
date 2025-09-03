temperatura = []

for i in range(7):
    num = int(input("digite um número para as temperaturas de cada dia da semana: ")) 
    temperatura.append(num)

soma = sum (temperatura)
quantidade = len(temperatura)

media = soma / quantidade

quente = max (temperatura)
frio = min (temperatura)

acima = 0 
for(temperatura) in (temperatura):
    if(temperatura) > media:
        acima += 1

print (f"a temperatura mais quente: {quente}")
print (f"a temperatura mais fria: {frio}")
print (f"a média das temperatura: {media:.2f}")
print (f"números acima da média: {acima}")