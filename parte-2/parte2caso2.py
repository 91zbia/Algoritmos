import math
distancias = []

for i in range(6):
    distancia = float(input(f"informe a distância da viagem {i+1} em Km: "))
    distancias.append(distancia)

distanciatotal = sum(distancias)
maiordistancia = max(distancias)
menordistancia = min(distancias)
mediadistancias = math.ceil(distanciatotal / len(distancias))

print(f"a distância total percorrida: {distanciatotal} km")
print(f"a maior distância percorrida: {maiordistancia} km")
print(f"a menor distância percorrida: {menordistancia} km")