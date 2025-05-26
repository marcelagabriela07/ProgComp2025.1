
# Entrada da primeira data
dia1 = int(input("Digite o dia da primeira data: "))
mes1 = int(input("Digite o mês da primeira data: "))

# Entrada da segunda data
dia2 = int(input("Digite o dia da segunda data: "))
mes2 = int(input("Digite o mês da segunda data: "))

# Define fevereiro com 28 dias (ano comum)
# o código está calculando quantos dias se passaram desde o início do ano até a primeira data.
if mes1 == 1:
    total1 = dia1
elif mes1 == 2:
    total1 = 31 + dia1
elif mes1 == 3:
    total1 = 31 + 28 + dia1
elif mes1 == 4:
    total1 = 31 + 28 + 31 + dia1
elif mes1 == 5:
    total1 = 31 + 28 + 31 + 30 + dia1
elif mes1 == 6:
    total1 = 31 + 28 + 31 + 30 + 31 + dia1
elif mes1 == 7:
    total1 = 31 + 28 + 31 + 30 + 31 + 30 + dia1
elif mes1 == 8:
    total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia1
elif mes1 == 9:
    total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia1
elif mes1 == 10:
    total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia1
elif mes1 == 11:
    total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia1
elif mes1 == 12:
    total1 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia1

# o código está calculando quantos dias se passaram desde o início do ano até a segunda data.
if mes2 == 1:
    total2 = dia2
elif mes2 == 2:
    total2 = 31 + dia2
elif mes2 == 3:
    total2 = 31 + 28 + dia2
elif mes2 == 4:
    total2 = 31 + 28 + 31 + dia2
elif mes2 == 5:
    total2 = 31 + 28 + 31 + 30 + dia2
elif mes2 == 6:
    total2 = 31 + 28 + 31 + 30 + 31 + dia2
elif mes2 == 7:
    total2 = 31 + 28 + 31 + 30 + 31 + 30 + dia2
elif mes2 == 8:
    total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia2
elif mes2 == 9:
    total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia2
elif mes2 == 10:
    total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia2
elif mes2 == 11:
    total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia2
elif mes2 == 12:
    total2 = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia2

# Calcular a diferença de dias
diferenca = total2 - total1

# Mostrar o resultado
print("Diferença de dias entre as datas:", diferenca)
