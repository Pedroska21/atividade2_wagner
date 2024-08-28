contador = 1
numero1 = 0
numero2 = 1
numero_seguinte = numero2
while contador <=14:
    print (numero_seguinte, end=" ")
    contador += 1
    numero1, numero2 = numero2, numero_seguinte
    numero_seguinte = numero1 + numero2
print()