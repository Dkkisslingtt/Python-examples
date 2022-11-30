Arqueros = ["Sergio Romero", "Wilfredo Caballero", "Nahuel Guzmán", "Franco Armani(T)"]
Defensores = ["Eduardo Salvio", "Gabriel Mercado(T)", "Nicolás Otamendi(T)", "Javier Mascherano", "Federico Fazio", "Marcos Rojo", "Marcos Acuña", "Ramiro Funes Mori", "Germán Pezzella(T)", "Cristian Ansaldi", "Nicolás Tagliafico(T)"]
Mediocampistas = ["Lucas Biglia", "Ever Banega", "Giovani Lo Celso(T)", "Manuel Lanzini", "Enzo Perez", "Pablo Perez", "Leandro Paredes(T)", "Guido Pizarro", "Rodrigo Battaglia", "Ricardo Centurión(T)", "Angel Di María", "Diego Perotti", "Maximiliano Meza"]
Delanteros = ["Paulo Dybala", "Sergio Agüero", "Gonzalo Higuaín", "Lionel Messi(T)", "Mauro Icardi", "Lautaro Martínez(T)", "Cristian Pavón(T)"]
procYpos = ["e-arq", "e-arq","e-arq", "l-arq", "e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-def","e-vol","e-vol","e-vol","e-vol","l-vol", "l-vol", "e-vol","e-vol",
"e-vol","l-vol", "e-vol","e-vol","l-vol", "e-del","e-del","e-del","e-del","e-del","l-del", "l-del"]
jugadores=Arqueros+Defensores+Mediocampistas+Delanteros
locales=[]
print ("el equipo titular es:")
for i in range (len(jugadores)):
    x=jugadores[i].find("(T)")
    y=jugadores[i].find(" ")
    if x>0: 
        titular=jugadores[i][y:x]
        print (titular)            
    if procYpos[i]=="l-arq" or procYpos[i]=="l-del":
        locales.append(jugadores[i][y:x]) 
print ("Locales que no son mediocampistas:")
for i in range (len(locales)):
    print (locales[i])