def laco():
    for multiplicador in range(1,11):
        numero = 1
        while numero <=10:
            resultado = multiplicador * numero
            print(f"{multiplicador} x {numero} = {resultado}")
            numero+=1
laco()