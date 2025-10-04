import os
os.system("cls")
class Clase():
    atributo_publico="soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atrbuto_privado="soy un atributo privado"

    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio



    def __getAtributoPrivado(self):
        return self.__atrbuto_privado
    
    def setAtributoPrivado(self,atributo_privado):
        self.__atrbuto_privado=atributo_privado

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self,tamanio):
        self.__tamanio=tamanio

        
    def getAtributoPrivado2(self):
        self.__getAtributoPrivado()

    #Usar los atributos y metodos de acuerdo a su encapsulamiento

objeto=Clase("Rojo","Grande")
print(f"Mi objeto tienene los siguientes atributos: {objeto.color} y {objeto.tamanio}")

print(f"Soy el contenido del atributo {objeto.atributo_publico}")

print(f"Soy el contenido del protegido {objeto._atributo_protegido}")

print(f"Soy el contenido del protegido {objeto.getAtributoPrivado2()}")

objeto.setAtributoPrivado("Se ha camniado el valor del atributo privado")

print(f"Soy el contenido del protegido {objeto.getAtributoPrivado()}")
