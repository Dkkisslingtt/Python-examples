

nombre=["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana", "Santamaria, Carlos", "Skarsgard, Azul", "Catalejos, Walter"]
sexo=["f", "f", "m", "f", "m", "f", "m"]
fecha=["02/05/1943", "07/09/1984", "10/02/1971", "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]
lista=[]
for i in range (len(nombre)):
   posi=nombre[i].find (",")
   x=nombre[i][posi+2]
   w=nombre[i][:posi]
   y=x[0]
   lista.append(y + "." + w)
print ("Iniciales y apellido de las personas: ")
for i in range (len (nombre)):
   print (lista[i])
lista2=[]
for i in range (len(nombre)):
   posi=nombre[i].find (",")
   x=nombre[i][posi+2:]
   lista2.append(x)

print (" ")
print (" ")

numeromayor=0
mayor= " "
for i in range (len(lista2)):
   x=(len(lista2[i]))
   if x>numeromayor:
      numeromayor=x
      mayor=lista2[i]
print ("El nombre más largo es:", mayor)

edades = []

for j in range (len(sexo)):
    if sexo[j] == "f":
        edades.append (fecha[j])



año=[]
año2=[]
dias=[]
dias2=[]
meses=[]
meses2=[]
for i in range (len(edades)):
   posi=edades[i].find("19")
   x=edades[i][posi:]
   año.append(x)
   y= int (año[i])
   año2.append(y)
for i in range (len(edades)):   
   posi2=edades[i].find ("/")
   w=edades[i][:posi2]
   dias.append(w)
   q=edades[i][posi+2]
   meses.append(q)
   a= int(dias[i])
   dias2.append(a)
   b= int (meses[i])
   meses2.append(b)


diaHoy = 27
mesHoy = 4
anioHoy = 2020

acumulador=0
for a in range(len(dias2)):
   edad = anioHoy - año2[a]
   if (meses2[a] > mesHoy) or (meses2[a] == mesHoy and dias2[a] > diaHoy):
      edad -= 1 # edad = edad - 1
   acumulador=acumulador + edad

print ("El promedio de edad de las mujeres es: ",acumulador/(len(año2)))