def numero ():
    
    while True:
        x=(input("ingrese un numero entero: "))
        try:
            x=int(x)
            break
        except ValueError:
            print("error en el dato ingresado")
            
    return x

print (numero())