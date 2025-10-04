import os
os.system("cls")

class Alumnos:
    #Metodo constructor que inicializa los valores de los atributos cuando se instancie un objeto de la clase
    def __init__(self,nombre,edad,matricula):
        self._nombre=nombre
        self._edad=edad
        self._matricula=matricula

    def inscribirse():
        return "inscrito"

    def estudiar():
        return "estudia"  


    def getNombre(self):
        return self._nombre
    
    def setNombre(self,Nuevo):
        self._nombre=Nuevo

    def getEdad(self):
        return self._edad
    
    def setEdad(self,Nuevo):
        self._edad=Nuevo

    def getMatricula(self):
        return self._matricula
    
    def setMatricula(self,Nuevo):
        self._matricula=Nuevo
    
    


class Profesores:
    #Metodo constructor que inicializa los valores de los atributos cuando se instancie un objeto de la clase
    def __init__(self,nombre,experiencia,num_profesor):
        self._nombre=nombre
        self._experiencia=experiencia
        self._num_profesor=num_profesor

    def impartir():
        return "Imparte"

    def evaluar():
        return "Evalua"

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,Nuevo):
        self._nombre=Nuevo

    def getExperiencia(self):
        return self._experiencia
    
    def setExperiencia(self,Nuevo):
        self._experiencia=Nuevo

    def getNum_Profe(self):
        return self._num_profesor
    
    def setNum_Profe(self,Nuevo):
        self._num_profesor=Nuevo
    
    



class Cursos:
    #Metodo constructor que inicializa los valores de los atributos cuando se instancie un objeto de la clase
    def __init__(self,nombre,codigo,creditos):
        self._nombre=nombre
        self._codigo=codigo
        self._creditos=creditos    

    def asignar():
        return "Asigna"           

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,Nuevo):
        self._nombre=Nuevo

    def getCodigo(self):
        return self._codigo
    
    def setCodigo(self,Nuevo):
        self._codigo=Nuevo

    def getCreditos(self):
        return self._creditos
    
    def setCreditos(self,Nuevo):
        self._creditos=Nuevo
    
    
  
alumno1= Alumnos("juan",18,123)  
alumno2= Alumnos("juana",18,124)

profesor1=Profesores("alan",10,1)
profesor2= Profesores("ana",10,2)

curso1= Cursos("matematicas","mate",5)
curso2= Cursos("ciencias","ciencia",5)

print (f"Alumnos {alumno1._nombre} {alumno2._nombre}")
print (f"Profesores {profesor1._nombre} {profesor2._nombre}")
print (f"Cursos {curso1._nombre} {curso2._nombre}")