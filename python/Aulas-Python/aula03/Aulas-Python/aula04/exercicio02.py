def exibir_menu():
    print("\n Tipo de instalacao: ")
    print("R - Residencia: ")
    print("C - Comercio: ")
    print("I - Industria: ")
    print("S - Sair: ")

def obter_tipo_instalcao():
    while True:
        tipo = input("Digite o tipo de instalacao ( R,C,I,S): ").strip().upper()
        if tipo in ("R","C","I","S"):
            return tipo
        print("Tipo de instalacao invalido. tente novamente")

def obter_faixa_kwh():
    while True:
        try:
            kwh = int(input("Digite a faixa de kwh consumida (ex: 500,1000,5000):"))
            if kwh > 0:
                return kwh
            else:
                print("A quantidade de kwh deve ser maio que zero:")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro")
def calcular_preco(tipo,kwh):
    match tipo:
        case "R":
            if kwh <= 500:
                return kwh * 0.40
            else:
                return kwh * 0.65
        case "C":
            if kwh <= 500:
                return kwh * 0.55
            else:
                return kwh * 0.60
        case "I":
            if kwh <= 500:
                return kwh* 0.55
            else:
                return kwh * 0.60
        case _:
            return 0.0
def main():
        while True:
            exibir_menu()
            tipo_instalacao = obter_tipo_instalcao()
            if tipo_instalacao == "S":
                print("ENCERRANDO O PROGRAMA")
                break
            faixa_kwk = obter_faixa_kwh()
            valor = calcular_preco(tipo_instalacao,faixa_kwk)
            print(f"O valor a pagar é R$ {valor:.2f}")
if __name__ == "__main__":
    main()