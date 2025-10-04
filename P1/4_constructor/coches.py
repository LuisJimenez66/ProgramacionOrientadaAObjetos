import os
os.system("cls")

class Coches:
    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas): 
        self.marca=marca
        self.color=color
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas

    '''
    Crear los metodos getters y setters. estos metodos son importates y necesarios en todas las clases 
    para que el programamdor interactue con los valores de los atributos a traves de estos metodos 
    digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar 
    o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.

    En teoria se deberian de crer un metodo Getters y Settter por cada atributo que contenga la clase 

    Los metodos set siempre regresan valor es decir el valor de la propiedad a traves del return.
    Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o 
    propiedad en cuestion
    '''
    #primer forma
    def get_Marca(self):
        return self.marca
    
    def set_Marca(self, marca):
        self.marca=marca
    
    #Segunda forma
    @property
    def marca2(self):
        return self.marca
    
    @marca2.setter
    def marca2 (self,marca):
        self.marca=marca



    def get_Color(self):
        return self.color
    
    def set_Color(self, color):
        self.color=color
    
    def get_Modelo(self):
        return self.modelo
    
    def set_Modelo(self, modelo):
        self.modelo=modelo
    
    def get_Velocidad(self):
        return self.velocidad
    
    def set_Velocidad(self, velocidad):
        self.velocidad=velocidad
    
    def get_Caballaje(self):
        return self.caballaje
    
    def set_Caballaje(self,caballaje):
        self.caballaje=caballaje
    
    def get_Plazas(self):
        return self.plazas
    
    def set_Plazas(self,plazas):
        self.plazas=plazas



    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        pass    
    def frenar(self):
        pass
#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",18,15,6)
coche3=Coches("Honda","","",0,0,0)
coche4=Coches("","","",0,0,0)
coche1.num_serie="801721823"

coche4.marca2="Volvo"

print(f"Datos del Vehiculo: \n Marca:{coche1.get_Marca()} \n color: {coche1.get_Color()} \n Modelo: {coche1.get_Modelo()} \n velocidad: {coche1.get_Velocidad()} \n caballaje: {coche1.get_Caballaje()} \n plazas: {coche1.get_Plazas()} \n Numero de serie: {coche1.num_serie}\n")



print(f"Datos del Vehiculo: \n Marca:{coche2.get_Marca()} \n color: {coche2.get_Color()} \n Modelo: {coche2.get_Modelo()} \n velocidad: {coche2.get_Velocidad()} \n caballaje: {coche2.get_Caballaje()} \n plazas: {coche2.get_Plazas()} \n")




print(coche3.marca2,"\n")

print(coche4.marca2)