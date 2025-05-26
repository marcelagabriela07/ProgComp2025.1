
# Faça um programa que pede ao aluno(a) que digite as duas notas da 1ª e da 2ª unidade.
# Essas notas são armazenadas nas variáveis n1 e n2.
n1 = float(input("Digite a nota do 1º bimestre: "))
n2 = float(input("Digite a nota do 2º bimestre: "))

# Agora calcule a média das duas notas.
# A nota da 1ª unidade tem peso 2.
# A nota da 2ª unidade tem peso 3.
media = (2 * n1 + 3 * n2) / 5

# Mostra a média
print("Média da disciplina (Media):", media)

# Verifica a situação com base na média
if media >= 60:  # Se a média for maior que 60, o aluno(a) está aprovado.
    print("Situação: aprovado")
elif media >= 20:  # Se a média for menor que 20, o aluno(a) está reprovado.
    print("Situação: prova final")  # Se a média está entre 20 e 59, o aluno(a) vai para a prova final.

    # Agora vamos saber o resultado final se foi aprovado, reprovado ou prova final.
    naf_minima = (300 - 3 * media) / 2  # Agora vamos calcular a média final da disciplina com a prova final.
    print("Para ser aprovado, precisa tirar no mínimo", naf_minima, "na prova final.")
else:
    print("Situação: reprovado") 