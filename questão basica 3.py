continuar_soma = 's'
while (continuar_soma == 's'):
    numero1 = int (input('Digite um numero:'))
    numero2 = int (input('Digite outro numero:'))
    resultado = numero1 + numero2
    print (f"{numero1}+{numero2}= {resultado}")
    continuar_soma = input ('Deseja fazer outra soma? [s ou n]')[:1]