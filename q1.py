 
# Faça um programa que pede pra digitar um numero inteiro
numero = int(input("Digite um número menor que 10000: "))

# Agora verifique se o numero é valido, se for menor que 10000, o programa continua.
if numero < 10000:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10

    # Agora some os quatro algarismos que foram separados.
    soma = unidade + dezena + centena + milhar
    print("Soma dos algarismos:", soma)

# Agora mostre o resultado se for mais de 10000, mostrar que é invalido.
# Se for menor que 10000, o resultado vai ser correto
else:
    print("Número inválido. Digite um número menor que 10000.")