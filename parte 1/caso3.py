impar = []
par = []

def numero():
    for i in range(10):
        num = int(input(f"digite o {i + 1}° numero: \n - "))

        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)

    print(f"quantidade de números pares: {len(par)}")
    print(f"quantidade de números impares: {len(impar)}")

numero()