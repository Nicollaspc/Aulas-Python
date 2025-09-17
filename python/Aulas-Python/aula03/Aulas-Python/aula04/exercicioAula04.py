def verificar_multa(velocidade:float) -> str:
    LIMITE_VELOCIDADE = 80
    MULTA_BASE = 100
    VALOR_KM = 15

    if velocidade > LIMITE_VELOCIDADE:
        km_acima = velocidade - LIMITE_VELOCIDADE
        valor_multa = MULTA_BASE + (km_acima * VALOR_KM)
        return f"Voce foi multado! O valor da multa é de R$ {valor_multa:.2f}"
    else:
        return "Voce esta dentro do limite de velocidade, nenhuma multa aplicada"
    valocidade = float(input("Digite a velocidade do carro (KM/H):"))
    resultado = verificar_multa(velocidade)
    print(resultado)