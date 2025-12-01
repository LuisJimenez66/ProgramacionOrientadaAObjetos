'''
Diciembre 1
    1)Implementacion de MVC
    2)POO
    3)Interfaces:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar_autos()

Productos entregarbles:
    Estructura del proyecto basado en MVC
    Modulo principal "main"
    Interaccion con las interfaces 
    Nombre del commit: "commit_01_12_25"
'''
from tkinter import *
from view import view1

class App:
    @staticmethod
    def main (ventana):
        view=view1.View(ventana)


if __name__=="__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()