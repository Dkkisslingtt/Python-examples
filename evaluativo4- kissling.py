nombres2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
nombres18M=["Emma","Olivia","Ava","Isabella","Sophia"]  
nombres18H=["Liam", "Noah", "Michael", "James", "Oliver"] 
numero18H=[19837,18267,14516,13525,13389]

numero18M=[18688,17921,14924,14464,13928]

def listas (texto):
    nombres=[]
    numeros=[]
    sexo=[]
    mujeres=[]
    hombres=[]
    nacimiento=[]
    nacimiento2=[]
    sexoM=[]
    sexoH=[]
    individuos=texto.split(",")
    for i in range (len(individuos)):
        if individuos[i].isalpha() and (len (individuos[i]))>2:
            nombres.append(individuos[i])
        elif individuos[i].isalpha() and (len (individuos[i]))<2:
            sexo.append(individuos[i])
        elif individuos[i].isdigit:
            numeros.append(individuos[i])
    for j in range (len(nombres)):
        if sexo[j]=="f":
            mujeres.append(nombres[j])
            nacimiento.append(numeros[j])
            sexoM.append(sexo[j])
        elif sexo[j]=="m":
            hombres.append(nombres[j])
            nacimiento2.append(numeros[j])
            sexoH.append(sexo[j])
    return (mujeres,sexoM,nacimiento,hombres,sexoH,nacimiento2)

def buscador(anio,posicion,sexo):
    lista2018=(nombres18H,numero18H,nombres18M,numero18M)
    try:
        nombres2018H,numero2018H,nombres2018M,numero2018M=lista2018
        mujeres2008,sexoM,numeroM,hombres2008,sexoH,numerosH= listas(nombres2008)
        resta=(posicion-1)
        if anio==2008:
            if sexo=="f":
                x= mujeres2008[resta]
                y= numeroM[resta]
            elif sexo== "m":
                x= hombres2008[resta]
                y= numerosH[resta]
        elif anio==2018:
            if sexo=="f":
                x= nombres2018M[resta]
                y= numero2018M[resta]
            elif sexo== "m":
                x= nombres2018H[resta]
                y= numero2018H[resta]

        return (x,y)
    except:
        x=("el programa no se ejecuto correctamente")
        return (x)

def BuscN (nombre, anio):

    mujeres2008,sexoM,numeroM,hombres2008,sexoH,numerosH= listas(nombres2008)           
    listanombres2008=[mujeres2008+hombres2008]
    listanombres2018=(nombres18H+nombres18M)
    y=" "
    w=" "
    NomMinus=nombre.lower()
    if anio==2008:
        for i in range (len (listanombres2008)):
            str1=" ".join(listanombres2008[i])
            y = (str1+" "+ y)
            minuscula= y.lower()
            x=NomMinus in minuscula
            return (x)

    elif anio==2018:
        for i in range (len (listanombres2018)):
            str2=" ".join(listanombres2018)
            w= (str2+" "+w)
            minuscula2=w.lower()
            a=NomMinus in minuscula2
            return (a)
    else:
        x="el año es incorrecto"
        return (x)

def dife (posi,sexo):
    mujeres2008,sexoM,numeroM,hombres2008,sexoH,numerosH= listas(nombres2008)
    posicion=(posi-1)
    ordenada=sorted(numeroM,reverse=True)
    ordenada2=sorted(numerosH,reverse=True)
    if sexo=="m":
        x=(int(ordenada2[posicion]))
        y=(int(numero18H[posicion]))
        resta=(x-y)
    elif sexo=="f":
        x=(int(ordenada[posicion]))
        y=(int(numero18M[posicion]))
        resta=(x-y)
    return resta

def busqueda (caracter):
    mujeres2008,sexoM,numeroM,hombres2008,sexoH,numerosH= listas(nombres2008)
    listanueva=(mujeres2008+hombres2008+nombres18M+nombres18H)
    listanueva1=[]
    for i in range (len(listanueva)):
        x=listanueva[i].find(caracter)
        if x>=0:
            listanueva1.append(listanueva[i])
    return (listanueva1)

def repetidos (nombre,nombre2,nombre3):
    mujeres2008,sexoM,numeroM,hombres2008,sexoH,numerosH= listas(nombres2008)
    listanueva=(mujeres2008+hombres2008+nombres18M+nombres18H)
    listanueva1=[]
    cont=0
    cont1=0
    cont2=0
    for i in range (len(listanueva)):
        if nombre==listanueva[i]:
            cont=(cont+1)
        if nombre2==listanueva[i]:
            cont1=(cont1+1)
        if nombre3==listanueva[i]:
            cont2=(cont2+1)
    if cont>1:
        listanueva1.append(nombre)
    if cont1>1:
        listanueva1.append(nombre2)
    if cont2>1:
        listanueva1.append(nombre3)
    return listanueva1

print (dife(1,"m"))
print (dife(2,"f"))
print(busqueda("J"))
print (repetidos("Emma","Daniel", "Olivia"))