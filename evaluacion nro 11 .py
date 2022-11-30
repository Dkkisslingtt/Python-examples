class Pelicula():
    def extraer_guardar_informacion(self):
        archivo = open("pelis.json", "r", encoding="utf8")
        date=archivo.read()        
        film=[]
        actors=[]
        rating=[]
        recaudaciones=[]
        l= round(date.__len__()/15)                                                                
        con=0                  
        for x in range(1,16):
            archivo.seek(con)                
            data=archivo.read(l)
            title=data.find('Title') 
            actor=data.find('Actors')
            ratings=data.find('Rotten Tomato')
            recaudacion1=data.find('BoxOffice')
            if title!= -1:
                corte=data.find("Year")               
                peli=data[title+8:corte].replace('"','').replace(',','').strip()               
                film.append(peli)                                                                                   
            elif actor != -1:             
                corte=data.find('Plot')
                actor=data[actor+9:corte].replace('"','').corte(',')[0].strip()             
                actors.append(actor)
            elif ratings != -1:                          
                corte=data.find('%"')
                rating=actor=data[ratings+42:corte].replace('"','').strip()
                rating.append(rating) 
            elif recaudacion1 != -1:
                corte=data.find('Production')
                recaudacion2=data[recaudacion1+13:corte].replace('"','').replace('$','').replace(',','').strip()               
                recaudaciones.append(recaudacion2) 	
            con=l*x
        open('pelis.txt','w').write('') #creamos un archivo porque los chicos decian que habia que crear uno          
        x=open('pelis.txt','a')       
        con=0
        while con < 3:        
           x.write('titulo:'+' '+film[con]+'\n'+'actor:'+' '+actors[con]+'\n'+'rating:'+' '+rating[con]+'\n'+'recaudacion:'+' '+recaudaciones[con]+'\n')       
           con+=1
        x.close()
class Menu():
    def Muestroopciones(self):
        dat=open("pelis.txt","r",encoding="utf8")
        c="hola"
        texto=""
        while c!="":
            c=dat.read()
            texto+=c
        dat.close()
        lista=texto.split('\n')
        print("Bienvenido" )
        print("utilice los numeros para elegir su opcion", '\n')
        print("1-Arrival") 
        print("2-Transcendence")
        print("3-Serenity")
        print("4-ver rating promedio")
        print("5-ver la recaudacion total",'\n')
        
        while True:
            try:
                opcion=int(input("cual es su opcion? "))
                if opcion<6 and opcion>0:
                    if opcion==1:
                        print(lista[0:4])
                        break
                    elif opcion==2:
                        print(lista[4:8])
                        break
                    elif opcion==3:
                        print(lista[9:12])
                        break
                    elif opcion==4:
                        nlista=[int(Numero) for Numero in texto.split() if Numero.isdigit()]
                        promedio=(nlista[0]+nlista[2]+nlista[4])/3
                        print(promedio)
                        break
                    elif opcion==5:
                        nlista=[int(Numero) for Numero in texto.split() if Numero.isdigit()]
                        todosr=(nlista[1]+nlista[3]+nlista[5])
                        print(todosr)
                        break
            except ValueError:
                    print("No es una opcion valida")
                    

j=Menu()
j.Muestroopciones()
