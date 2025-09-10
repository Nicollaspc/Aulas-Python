def ordem(a: int, b: int, c:int) -> None:
    if(a > b):
        a,b =b,c
    if(a > c):
        a,c = c,a
    if(b > c):
        b,c = c,b
    print(f"\n10. valor : {a}")
    print(f"\n20. valor : {b}")
    print(f"\n10. valor : {c}")


if __name__ == "__main__":
    a = int(input("Informe o 10. valor: "))
    b= int(input("Informe o 10. valor: "))
    c= int(input("Informe o 10. valor: "))
    ordem(a,b,c)