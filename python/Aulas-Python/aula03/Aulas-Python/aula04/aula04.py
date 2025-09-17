    
while True:
    nome = input("Nome: ")
    if len(nome)==0:
        continue
    if nome == "-1":
        break
    n1= float(input("Nota da primeira prova: "))
    n2 = float(input("Nota da segunda prova:"))
    media = (n1+n2)/2
    if media > 7:
        print(f"O aluno {nome} fo aprovado com media {media}")
    else:
        print(f"O aluno {nome} foi reprovado com media {media}")
