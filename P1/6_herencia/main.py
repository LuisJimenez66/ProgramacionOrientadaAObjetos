from coches import *
import os
os.system("cls")

#Solicitar los datos que posteriormente seran los atributos del objeto



'''

num_coches=int(input("Cuantos coches tienes? "))

for i in range (0,num_coches):

    print(f"\n\t..::Datos del Automovil::.. {i+1}")
    marca=input("Ingresa la marca: ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("Ingresa el modelo: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plazas=int(input("Ingresa el # de plazas: "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"Datos del Vehiculo {i+1}: \n Marca:{coche1.get_Marca()} \n color: {coche1.get_Color()} \n Modelo: {coche1.get_Modelo()} \n velocidad: {coche1.get_Velocidad()} \n caballaje: {coche1.get_Caballaje()} \n plazas: {coche1.get_Plazas()} \n \n")

'''
'''coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",18,15,6)
coche3=Coches("Honda","","",0,0,0)
coche4=Coches("","","",0,0,0)
coche1.num_serie="801721823"

coche4.marca2="Volvo"

print(f"Datos del Vehiculo: \n Marca:{coche1.get_Marca()} \n color: {coche1.get_Color()} \n Modelo: {coche1.get_Modelo()} \n velocidad: {coche1.get_Velocidad()} \n caballaje: {coche1.get_Caballaje()} \n plazas: {coche1.get_Plazas()} \n Numero de serie: {coche1.num_serie}\n")



print(f"Datos del Vehiculo: \n Marca:{coche2.get_Marca()} \n color: {coche2.get_Color()} \n Modelo: {coche2.get_Modelo()} \n velocidad: {coche2.get_Velocidad()} \n caballaje: {coche2.get_Caballaje()} \n plazas: {coche2.get_Plazas()} \n")




print(coche3.marca2,"\n")

print(coche4.marca2)'''
coche=Coches("VW","Blanco","2020",220,180,4)
camion=Camiones("VW","Blanco aperlado","2020",220,180,4,2,2500)
camioneta=Camionetas("VW","Azul","2020",220,180,4,"delantera",True)

print(coche.color, coche.acelerar())
print(camion.color,camion.acelerar())
print(camioneta.color,camioneta.acelerar())