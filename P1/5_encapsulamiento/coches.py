import os
os.system("cls")

class Coches:
    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas): 
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

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
        return self.__marca
    
    def set_Marca(self, marca):
        self.__marca=marca
    
    #Segunda forma
    @property
    def marca2(self):
        return self.__marca
    
    @marca2.setter
    def marca2 (self,marca):
        self.__marca=marca



    def get_Color(self):
        return self.__color
    
    def set_Color(self, color):
        self.__color=color
    
    def get_Modelo(self):
        return self.__modelo
    
    def set_Modelo(self, modelo):
        self.__modelo=modelo
    
    def get_Velocidad(self):
        return self.__velocidad
    
    def set_Velocidad(self, velocidad):
        self.__velocidad=velocidad
    
    def get_Caballaje(self):
        return self.__caballaje
    
    def set_Caballaje(self,caballaje):
        self.__caballaje=caballaje
    
    def get_Plazas(self):
        return self.__plazas
    
    def set_Plazas(self,plazas):
        self.__plazas=plazas



    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        return  "Estas acelerando"
    def frenar(self):
        return "estas frenando"
#Fin definir clase

#Crear un objetos o instanciar la clase

