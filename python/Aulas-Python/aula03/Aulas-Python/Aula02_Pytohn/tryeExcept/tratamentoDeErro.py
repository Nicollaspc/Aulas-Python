try:
    num1 = int(input("Digite o primeiro numero: \n"))
    num2 = int(input("Digite o segundo numero: \n"))

    if num2==0:
        print("Erro: Nao é possivel dividir por zero")
    else:
        resultado = num1 / num2
        print(f"Resultado da divisao: {resultado}")
except ValueError:
    print(f"Erro: Voce deve digitar apenas numero")


    