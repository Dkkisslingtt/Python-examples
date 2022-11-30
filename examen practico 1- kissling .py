
genero=["B","B","B","S","S"]
bandas=["Led Zeppelin","Rage Against the Machine","Seru Giran","Peter Gabriel","Jeff Beck"]
albunes=[9,4,5,10,3]
miembros=["Jimmy Page", "Robert Plant (voz)", "John Bonham", "John Paul Jones","Zack de la Rocha (voz)","Tom Morello","Tim Commerford","Brad Wilk","Pedro Aznar","Oscar Moro", "David Lebón (voz)", "Charly García (voz)"]
vp= [1234567,2434908,324192,70,76]

class Composicion():
	def datos (self,nombre,albunes):
		self.nombre=nombre
		self.albun=albunes
class Bandas(Composicion):
	def __init__(self,visualizacion):
		self.visualizacion=visualizacion
class Solistas(Composicion):
	def __init__ (self,edad):
		self.edad=edad
class Spotify ():
	def contador (self):
		conta=0
		for i in range(len(vp)):
			if genero[i]=="B":
				x=Bandas(vp[i])
				conta=x.visualizacion+conta
		return (conta) 
	def apellidodesolistas (self):
		for i in range (len(genero)):
			ApeSolista=[]
			if genero[i]=="S":
				y=Solistas(vp[i])
				y.datos(bandas[i],albunes[i])
				w=y.nombre.find(" ")
				if w>1:
					ApeSolista.append(y.nombre[w+1:])
				print (ApeSolista)
	def vocalistas(self):
		for i in range(len(vp)):
			nomvocal=[]
			if genero[i]=="B":
				z=Bandas(vp[i])
				for e in range(len (miembros)):
					z.datos(miembros[e],albunes[i])
					vocal=z.nombre.find("(voz)")
					if vocal>0:
						nomvocal.append(z.nombre[:vocal])
				return nomvocal					
	def mayor1(self):
		mayo=0
		for i in range (len(albunes)):
			masmejor=[]
			x=Solistas(vp[i])
			x.datos(bandas[i],albunes[i])
			if x.albun>mayo:
				mayo=x.albun
				if mayo==10:
					masmejor.append(x.nombre)
					return masmejor
r=Spotify()
print (r.contador())
print (r.apellidodesolistas())
print(r.vocalistas())
print (r.mayor1())

		
		