comando = input("Digite uma mensagem: \n")
match comando.upper():
    case 'OI':
        print("Olá meu amigo")
    case 'TCHAU':
        print("Ate logo")
    case _:
        print("Dado nao encontrado")