
# Faça um programa que solicite ao usuário o tempo de permanência em minutos
minutos = int(input("Digite o tempo de permanência no estacionamento (em minutos): "))

# Mudar minutos para horas, arredondando para cima se houver minutos extras
if minutos % 60 == 0:
    horas = minutos // 60  
else:
    horas = minutos // 60 + 1  

#  Agora calculamos o preço com base no número de horas
if horas > 12:
    preco = 30.00  
elif horas <= 2:
    preco = horas * 8  
elif horas <= 4:
    preco = (2 * 8) + (horas - 2) * 5  
else:
    preco = (2 * 8) + (2 * 5) + (horas - 4) * 3  

# Exibe o valor a pagar
print("Valor a pagar: R$", preco)