def tente(idade_text: str) -> None:
    try:
        idade = int(idade_text)
        if idade < 0:
            print("idade nao pode ser negativa. tente novamente.")
        print(f"idade Registrada: {idade}")
    except ValueError:
        print("Entrada invalida,tente novamente")
def menor_que_50(valor):
    if not (valor > 50):
        print(f"\n Valor = {valor}")

if __name__ == "__main__":
    texto = input("Digite a sua idade: ")
    n = int(input("Informe um valor numerico inteiro: "))
    tente(texto)
    menor_que_50(n)

