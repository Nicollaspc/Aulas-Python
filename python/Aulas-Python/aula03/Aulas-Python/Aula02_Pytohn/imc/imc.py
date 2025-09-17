try:
    peso = float(input("Digite o seu peso: \n"))
    altura = float(input("Digite a sua altura: \n"))
    imc = peso/(altura*altura)
    print("------------------------------------")
    print(f"Seu IMC é igual a {imc: .2f} ")
    print("------------------------------------")
    if imc<18.5:
        print("Classificacao: Abaixo do peso")
    elif imc < 24.9:
        print("Classificacao: Peso normal")
    elif imc < 29.9:
        print("Classificacao: Sobrepeso")
    elif imc < 34.9:
        print("Classificacao: Obesidade Grau 1")
    elif imc < 39.9:
        print("Classificacao: Obesidade Grau 2")
    else:
        print("Classificacao: Obesidade Grau 3")
except ValueError:
    print("Erro")