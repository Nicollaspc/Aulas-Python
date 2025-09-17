response_code = 404

match response_code:
    case 400:
        print("Server sem resposta")
    case 401 | 403:
        print("Server se recusa a enviar retorno")
    case 404:
        print("Server nao encontrado")