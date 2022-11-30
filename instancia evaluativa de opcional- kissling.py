personas="juan-m-1.78-marron-castaño/pedro-m-1.68-marron-castaño/julia-f-1.71-verde-rubio/ana-f-1.65-verde-rubio/josé-m-1.90-verde-rubio/camila-f-1.73-verde-rubio/laura-f-1.63-verde-rubio/sara-f-1.69-celeste-rubia"
lista=[]
individuos=personas.split("/")
nombre=[]
sexo=[]
pelo=[]
altura=[]
medida=[]
nombrefinal=[]
contador=0
contador2=0
acumu=0
for i in range (len(individuos)):
    posi=individuos[i].find ("-")
    posi2=individuos[i].find ("1")
    name=individuos[i][:posi]
    nombre.append(name)
    sex=individuos[i][posi+1]
    sexo.append(sex)
    color_de_pelo=individuos[i][posi+8:]
    pelo.append(color_de_pelo)
    high=individuos[i][posi2:posi2+4]
    altura.append(high)
for i in range (len(altura)):
    x=float(altura[i])
    medida.append(x)
    if medida[i]>=1.70 and medida[i]<=1.80:
        y=nombre[i]
        acumu=acumu+medida[i]
        contador2=contador2+1
        promedio=acumu/(contador2)
        nombrefinal.append(y)
    if sexo[i]=="f" and pelo[i]=="verde-rubio":
        contador=contador+1     
print (" ")
print ("La altura promedio del primer grupo es:", promedio, "y sus nombres son", nombrefinal)
print(" ")
print ("La cantidad de personas del segundo grupo es: ", contador)
#agrege la opcion contraria a split para dar un final en forma de 
#string a los nombres en ves de lista
#y el promedio nose porque me dio asi
nombrefinalstring=",".join(nombrefinal)
print(" ")
print ("La altura promedio del primer grupo es:", promedio, "y sus nombres son", nombrefinalstring)
print (" ")
