def numero ():
    while True:
        x=(input("ingrese un numero real: "))
        try:
            x=float(x)
            break
        except ValueError:
            print("error en el dato ingresado")
            
    return x

print (numero())