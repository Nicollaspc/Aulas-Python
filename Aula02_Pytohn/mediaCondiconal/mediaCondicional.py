print("-----------------------------------------------")
nome = input("Digite o seu nome: \n")
print("-----------------------------------------------")
nota1 = float(input("Digite a primeira nota: \n"))
print("-----------------------------------------------")
nota2 = float(input("Digite a segunda nota: \n"))

media = (nota1 + nota2) / 2
print("-----------------------------------------------")
if media >= 6:
    print(f"O aluno {nome} está aprovado com media igual a {media: .2f}")

elif media >= 4:
     print(f"O Aluno {nome} está em exame final com media igual a {media: .2f}")

else:
     print(f"O Aluno {nome} está reprovado com media igual a {media: .2f}")
print("-----------------------------------------------")