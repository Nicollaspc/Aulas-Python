def aluno():
        nome = input("Digite o seu nome: \n")
        nota1= float(input("Digite a primeira nota: \n"))
        nota2 = float(input("Digite a segunda nota: \n"))
        media = (nota1 + nota2) / 2

        if media >= 6:
            print(f"{nome}Aprovado com media = {media}")
        else:
            print(f"{nome}reprovado com media = {media}")
aluno()
