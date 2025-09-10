total,cont,media_turma,soma = 2,1,0,0
while cont <= total:
    nome = input("Nome: ")
    n1 = float(input("Nota de primeira prova: "))
    n2 = float(input("Digite a segunda prova"))
    media = (n1 + n2) / 2
    if media >= 7:
        print(f"O aluno {nome} foi aprovado com media {media}")
    else:
        print(f"O aluno {nome} foi reprovado com media {media}")
        soma+=media
    cont +=1

media_turma = soma / total
print(f"A media da turma foi de {media_turma}")