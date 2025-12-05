from tkinter import *
from tkinter import messagebox
from controller import controlador
class View():
    def __init__(self,ventana):
        ventana.title("Coches system")
        ventana.geometry("1000x800")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrar_pantalla(ventana):
        for i in ventana.winfo_children():
            i.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text="Bienvenido a cohes system")
        lbl_titulo.pack(pady=10)
        btn_coches=Button(ventana, text="Coches", command=lambda:View.menu_acciones(ventana,"Coches"))    
        btn_coches.pack(pady=5)
        btn_camionetas=Button(ventana, text="Camionetas", command=lambda:View.menu_acciones(ventana,"Camionetas")) 
        btn_camionetas.pack(pady=5)
        btn_camiones=Button(ventana, text="Camiones", command=lambda:View.menu_acciones(ventana,"Camiones")) 
        btn_camiones.pack(pady=5)
        btn_salir=Button(ventana, text="Salir", command=ventana.destroy)
        btn_salir.pack(pady=5)

    @staticmethod
    def menu_acciones(ventana,tipo):
        View.borrar_pantalla(ventana)
        if tipo=="Coches":
            lbl_titulo=Label(ventana, text=f"Bienvenido al menu de {tipo}")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana, text="Insertar", command=lambda:View.insertar_coches(ventana,tipo))    
            btn_insertar.pack(pady=5)
            btn_mostrar=Button(ventana, text="Mostrar", command=lambda:View.consultar_autos(ventana,tipo)) 
            btn_mostrar.pack(pady=5)
            btn_Modificar=Button(ventana, text="Modificar", command=lambda:View.cambiar_autos(ventana,tipo)) 
            btn_Modificar.pack(pady=5)   
            btn_Eliminar=Button(ventana, text="Eliminar", command=lambda:View.eliminar_autos(ventana,tipo)) 
            btn_Eliminar.pack(pady=5)   
            btn_volver=Button(ventana, text="Regresar", command=lambda:View.menu_principal(ventana)) 
            btn_volver.pack(pady=5)  
        elif tipo=="Camiones":
            lbl_titulo=Label(ventana, text=f"Bienvenido al menu de {tipo}")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana, text="Insertar", command=lambda:View.insertar_camiones(ventana,tipo))    
            btn_insertar.pack(pady=5)
            btn_mostrar=Button(ventana, text="Mostrar", command=lambda:View.consultar_camiones(ventana,tipo)) 
            btn_mostrar.pack(pady=5)
            btn_Modificar=Button(ventana, text="Modificar", command=lambda:View.cambiar_camiones(ventana,tipo)) 
            btn_Modificar.pack(pady=5)   
            btn_Eliminar=Button(ventana, text="Eliminar", command=lambda:View.eliminar_camiones(ventana,tipo)) 
            btn_Eliminar.pack(pady=5)   
            btn_volver=Button(ventana, text="Regresar", command=lambda:View.menu_principal(ventana))
            btn_volver.pack(pady=5)  
        elif tipo=="Camionetas":
            lbl_titulo=Label(ventana, text=f"Bienvenido al menu de {tipo}")
            lbl_titulo.pack(pady=10)
            btn_insertar=Button(ventana, text="Insertar", command=lambda:View.insertar_camionetas(ventana,tipo))    
            btn_insertar.pack(pady=5)
            btn_mostrar=Button(ventana, text="Mostrar", command=lambda:View.consultar_camionetas(ventana,tipo)) 
            btn_mostrar.pack(pady=5)
            btn_Modificar=Button(ventana, text="Modificar", command=lambda:View.cambiar_camionetas(ventana,tipo)) 
            btn_Modificar.pack(pady=5)   
            btn_Eliminar=Button(ventana, text="Eliminar", command=lambda:View.eliminar_camionetas(ventana,tipo)) 
            btn_Eliminar.pack(pady=5)   
            btn_volver=Button(ventana, text="Regresar", command=lambda:View.menu_principal(ventana))    
            btn_volver.pack(pady=5)        

    @staticmethod
    def insertar_coches(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a insertar {tipo}")
        lbl_titulo.pack(pady=10)

        lbl_marca=Label(ventana,text="Ingresa la marca")
        lbl_marca.pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Ingresa la color")
        lbl_color.pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Ingresa el modelo")
        lbl_modelo.pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Ingresa la velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caba=Label(ventana,text="Ingresa la caballaje")
        lbl_caba.pack(pady=5)
        txt_caba=Entry(ventana)
        txt_caba.pack(pady=5)

        lbl_plazas=Label(ventana,text="Ingresa el no de plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)
        btn_insertar=Button(ventana,text="Insertar", command=lambda:controlador.Controlador.insertar_coches(txt_color.get(),txt_marca.get(),txt_modelo.get(), txt_velocidad.get(),txt_caba.get(),txt_plazas.get())) 
        btn_insertar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5)   

    @staticmethod
    def consultar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a consultar coches"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=controlador.Controlador.consultar_coches()
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nAuto: {num_nota} \n ID: {i[0]} -Color: {i[1]} Marca: {i[2]} Modelo: {i[3]} \n Velocidad: {i[4]} Caballaje: {i[5]} Plazas: {i[6]}\n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a cambiar coches"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del coche a cambiar"))
        lbl_id.pack(pady=5)     
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()
        btn_buscar=Button(ventana,text="Buscar", command=lambda:controlador.Controlador.check_coches(ventana,tipo,id.get())) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_autos2(ventana,tipo,id,color,marca,modelo,velocidad,caballaje,plazas):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a actualizar {tipo}")
        lbl_titulo.pack(pady=10)

        var_id = StringVar()
        var_color = StringVar()
        var_marca = StringVar()
        var_modelo = StringVar()
        var_velocidad = StringVar()
        var_caballaje = StringVar()
        var_plazas = StringVar()

        # Asignamos valores iniciales
        var_id.set(id)
        var_color.set(color)
        var_marca.set(marca)
        var_modelo.set(modelo)
        var_velocidad.set(velocidad)
        var_caballaje.set(caballaje)
        var_plazas.set(plazas)

        # ID (solo lectura)
        lbl_id = Label(ventana, text="Id del coche:")
        lbl_id.pack(pady=5)
        txt_id = Entry(ventana, textvariable=var_id, state="disabled")
        txt_id.pack(pady=5)



        lbl_color = Label(ventana, text="Ingresa el color")
        lbl_color.pack(pady=5)
        txt_color = Entry(ventana, textvariable=var_color)
        txt_color.pack(pady=5)

        lbl_marca = Label(ventana, text="Ingresa la marca")
        lbl_marca.pack(pady=5)
        txt_marca = Entry(ventana, textvariable=var_marca)
        txt_marca.pack(pady=5)

        lbl_modelo = Label(ventana, text="Ingresa el modelo")
        lbl_modelo.pack(pady=5)
        txt_modelo = Entry(ventana, textvariable=var_modelo)
        txt_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Ingresa la velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velocidad = Entry(ventana, textvariable=var_velocidad)
        txt_velocidad.pack(pady=5)

        lbl_caba = Label(ventana, text="Ingresa la caballaje")
        lbl_caba.pack(pady=5)
        txt_caba = Entry(ventana, textvariable=var_caballaje)
        txt_caba.pack(pady=5)

        lbl_plazas = Label(ventana, text="Ingresa el no de plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas = Entry(ventana, textvariable=var_plazas)
        txt_plazas.pack(pady=5)
        btn_actualizar=Button(ventana,text="Actualizar",command=lambda:controlador.Controlador.cambiar_coches(var_color.get(),var_marca.get(),var_modelo.get(),var_velocidad.get(),var_caballaje.get(),var_plazas.get(),var_id.get())) 
        btn_actualizar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.cambiar_autos(ventana,tipo)) 
        btn_volver.pack(pady=5)

    @staticmethod
    def eliminar_autos(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a eliminar coches"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del coche a eliminar"))
        id=IntVar()
        lbl_id.pack(pady=5) 
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()          
        btn_buscar=Button(ventana,text="Buscar", command=lambda:controlador.Controlador.check_coches2(ventana,tipo,id.get())) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    def eliminar_autos2(ventana,tipo,id,color,marca,modelo,velocidad,caballaje,plazas):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Coche a eliminar: "))
        lbl_titulo.pack(pady=5) 
        filas=""

        filas=filas+f"\n ID: {id} -Color: {color} Marca: {marca} Modelo: {modelo} \n Velocidad: {velocidad} Caballaje: {caballaje} Plazas: {plazas}\n"

        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_borrar=Button(ventana,text="Borrar", command=lambda:controlador.Controlador.eliminar_coches(id)) 
        btn_borrar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.eliminar_autos(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    @staticmethod
    def insertar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a insertar {tipo}")
        lbl_titulo.pack(pady=10)

        lbl_color=Label(ventana,text="Ingresa la color")
        lbl_color.pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_marca=Label(ventana,text="Ingresa la marca")
        lbl_marca.pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=5)

        lbl_modelo=Label(ventana,text="Ingresa el modelo")
        lbl_modelo.pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Ingresa la velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caba=Label(ventana,text="Ingresa la caballaje")
        lbl_caba.pack(pady=5)
        txt_caba=Entry(ventana)
        txt_caba.pack(pady=5)

        lbl_plazas=Label(ventana,text="Ingresa el no de plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

        if tipo=="Camionetas":
            lbl_traccion=Label(ventana,text="Ingresa la traccion")
            lbl_traccion.pack(pady=5)
            txt_traccion=Entry(ventana)
            txt_traccion.pack(pady=5)

            lbl_plazas=Label(ventana,text="Selecciona una opcion")
            lbl_plazas.pack(pady=5)
            opcion = StringVar()
            opcion1 = Radiobutton(ventana,text="Cerrada",variable=opcion,value=False)
            opcion1.pack()
            opcion2 = Radiobutton(ventana,text="Abierta",variable=opcion,value=True)
            opcion2.pack()
            bnt_insertar_camionetas=Button(ventana,text="Insertar", command=lambda:controlador.Controlador2.insertar_camionetas(txt_color.get(),txt_marca.get(),txt_modelo.get(),txt_velocidad.get(),txt_caba.get(),txt_plazas.get(),txt_traccion.get(),opcion.get()))
            bnt_insertar_camionetas.pack(pady=5)
            
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5)   

    @staticmethod
    def consultar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a consultar camionetas"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=controlador.Controlador2.consultar_camionetas()
        num_camio=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nCamioneta: {num_camio} \n ID: {i[0]} -Color: {i[1]} Marca: {i[2]} Modelo: {i[3]}  Velocidad: {i[4]} \nCaballaje: {i[5]} Plazas: {i[6]} Traccion: {i[7]} Cerrada: {i[8]} \n"
                num_camio=num_camio+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay coches registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a cambiar camionetas"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id de la camioneta a cambiar"))
        id=IntVar()
        lbl_id.pack(pady=5)     
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()
        btn_buscar=Button(ventana,text="Buscar", command=lambda:controlador.Controlador2.check_camionetas(ventana,tipo,id.get())) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_camionetas2(ventana,tipo,id,color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a actualizar {tipo}")
        lbl_titulo.pack(pady=10)

        var_id = StringVar()
        var_color = StringVar()
        var_marca = StringVar()
        var_modelo = StringVar()
        var_velocidad = StringVar()
        var_caballaje = StringVar()
        var_plazas = StringVar()
        var_traccion= StringVar()
        var_cerrada= StringVar()

        # Asignamos valores iniciales
        var_id.set(id)
        var_color.set(color)
        var_marca.set(marca)
        var_modelo.set(modelo)
        var_velocidad.set(velocidad)
        var_caballaje.set(caballaje)
        var_plazas.set(plazas)
        var_traccion.set(traccion)
        var_cerrada.set(cerrada)

        # ID (solo lectura)
        lbl_id = Label(ventana, text="Id de la camioneta:")
        lbl_id.pack(pady=5)
        txt_id = Entry(ventana, textvariable=var_id, state="disabled")
        txt_id.pack(pady=5)



        lbl_color = Label(ventana, text="Ingresa el color")
        lbl_color.pack(pady=5)
        txt_color = Entry(ventana, textvariable=var_color)
        txt_color.pack(pady=5)

        lbl_marca = Label(ventana, text="Ingresa la marca")
        lbl_marca.pack(pady=5)
        txt_marca = Entry(ventana, textvariable=var_marca)
        txt_marca.pack(pady=5)

        lbl_modelo = Label(ventana, text="Ingresa el modelo")
        lbl_modelo.pack(pady=5)
        txt_modelo = Entry(ventana, textvariable=var_modelo)
        txt_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Ingresa la velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velocidad = Entry(ventana, textvariable=var_velocidad)
        txt_velocidad.pack(pady=5)

        lbl_caba = Label(ventana, text="Ingresa la caballaje")
        lbl_caba.pack(pady=5)
        txt_caba = Entry(ventana, textvariable=var_caballaje)
        txt_caba.pack(pady=5)

        lbl_plazas = Label(ventana, text="Ingresa el no de plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas = Entry(ventana, textvariable=var_plazas)
        txt_plazas.pack(pady=5)

        lbl_traccion=Label(ventana,text="Ingresa la traccion")
        lbl_traccion.pack(pady=5)
        txt_traccion=Entry(ventana, textvariable=var_traccion)
        txt_traccion.pack(pady=5)

        lbl_cerrada=Label(ventana,text="Cerrada?")
        lbl_cerrada.pack(pady=5)
        txt_cerrada=Entry(ventana, textvariable=var_cerrada)
        txt_cerrada.pack(pady=5)

        if var_cerrada.get()=="1" or var_cerrada.get()=="si":
            var_cerrada.set(True)
        else:
            var_cerrada.set(False)
                

        btn_actualizar=Button(ventana,text="Actualizar",command=lambda:controlador.Controlador2.cambiar_camionetas(var_color.get(),var_marca.get(),var_modelo.get(),var_velocidad.get(),var_caballaje.get(),var_plazas.get(),var_traccion.get(),var_cerrada.get(),var_id.get())) 
        btn_actualizar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.cambiar_camionetas(ventana,tipo)) 
        btn_volver.pack(pady=5)   
     
    @staticmethod
    def eliminar_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a eliminar camionetas"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id de la camioneta a eliminar"))
        lbl_id.pack(pady=5) 
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()          
        btn_buscar=Button(ventana,text="Buscar", command=lambda:controlador.Controlador2.check_camionetas2(ventana,tipo,id.get())) 
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    def eliminar_camionetas2(ventana,tipo,id,color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Camioneta a eliminar"))
        lbl_titulo.pack(pady=5) 
        filas=""

        
        filas=filas+f"\n ID: {id} -Color: {color} Marca: {marca} Modelo: {modelo}  Velocidad: {velocidad} \nCaballaje: {caballaje} Plazas: {plazas} Traccion: {traccion} Cerrada: {cerrada} \n"

        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_borrar=Button(ventana,text="Borrar",command=lambda:controlador.Controlador2.eliminar_camionetas(id)) 
        btn_borrar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.eliminar_camionetas(ventana,tipo)) 
        btn_volver.pack(pady=5)
    @staticmethod
    def insertar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a insertar {tipo}")
        lbl_titulo.pack(pady=10)

        lbl_color=Label(ventana,text="Ingresa la color")
        lbl_color.pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_marca=Label(ventana,text="Ingresa la marca")
        lbl_marca.pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=5)

        lbl_modelo=Label(ventana,text="Ingresa el modelo")
        lbl_modelo.pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Ingresa la velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caba=Label(ventana,text="Ingresa la caballaje")
        lbl_caba.pack(pady=5)
        txt_caba=Entry(ventana)
        txt_caba.pack(pady=5)

        lbl_plazas=Label(ventana,text="Ingresa el no de plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

        if tipo=="Camiones":
            lbl_eje=Label(ventana,text="Ingresa el eje")
            lbl_eje.pack(pady=5)
            txt_eje=Entry(ventana)
            txt_eje.pack(pady=5)

            lbl_carga=Label(ventana,text="Ingresa la capacidad de carga")
            lbl_carga.pack(pady=5)
            txt_carga=Entry(ventana)
            txt_carga.pack(pady=5)

            bnt_insertar_camiones=Button(ventana,text="Insertar",command=lambda:controlador.Controlador3.insertar_camiones(txt_color.get(),txt_marca.get(),txt_modelo.get(),txt_velocidad.get(),txt_caba.get(),txt_plazas.get(),txt_eje.get(),txt_carga.get()))
            bnt_insertar_camiones.pack(pady=5)
    
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5)   

    @staticmethod
    def consultar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a consultar camiones"))
        lbl_titulo.pack(pady=5) 
        filas=""
        registros=controlador.Controlador3.consultar_camiones()
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nCamioneta: {num_nota} \n ID: {i[0]} -Color: {i[1]} Marca: {i[2]} Modelo: {i[3]}  Velocidad: {i[4]} \nCaballaje: {i[5]} Plazas: {i[6]} Eje: {i[7]} Capacidad de carga: {i[8]} \n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No hay camiones registrados...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 


    @staticmethod
    def cambiar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a cambiar camiones"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del camion a cambiar"))
        lbl_id.pack(pady=5)     
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()
        btn_buscar=Button(ventana,text="buscar", command=lambda:controlador.Controlador3.check_camiones(ventana,tipo,id.get())) 
        btn_buscar.pack(pady=5) 
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    @staticmethod
    def cambiar_camiones2(ventana,tipo,id,color,marca,modelo,velocidad,caballaje,plazas,eje,capacidad):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Bienvenido a actualizar {tipo}")
        lbl_titulo.pack(pady=10)

        var_id = StringVar()
        var_color = StringVar()
        var_marca = StringVar()
        var_modelo = StringVar()
        var_velocidad = StringVar()
        var_caballaje = StringVar()
        var_plazas = StringVar()
        var_eje= StringVar()
        var_capacidad= StringVar()

        # Asignamos valores iniciales
        var_id.set(id)
        var_color.set(color)
        var_marca.set(marca)
        var_modelo.set(modelo)
        var_velocidad.set(velocidad)
        var_caballaje.set(caballaje)
        var_plazas.set(plazas)
        var_eje.set(eje)
        var_capacidad.set(capacidad)

        # ID (solo lectura)
        lbl_id = Label(ventana, text="Id de la camioneta:")
        lbl_id.pack(pady=5)
        txt_id = Entry(ventana, textvariable=var_id, state="disabled")
        txt_id.pack(pady=5)



        lbl_color = Label(ventana, text="Ingresa el color")
        lbl_color.pack(pady=5)
        txt_color = Entry(ventana, textvariable=var_color)
        txt_color.pack(pady=5)

        lbl_marca = Label(ventana, text="Ingresa la marca")
        lbl_marca.pack(pady=5)
        txt_marca = Entry(ventana, textvariable=var_marca)
        txt_marca.pack(pady=5)

        lbl_modelo = Label(ventana, text="Ingresa el modelo")
        lbl_modelo.pack(pady=5)
        txt_modelo = Entry(ventana, textvariable=var_modelo)
        txt_modelo.pack(pady=5)

        lbl_velocidad = Label(ventana, text="Ingresa la velocidad")
        lbl_velocidad.pack(pady=5)
        txt_velocidad = Entry(ventana, textvariable=var_velocidad)
        txt_velocidad.pack(pady=5)

        lbl_caba = Label(ventana, text="Ingresa la caballaje")
        lbl_caba.pack(pady=5)
        txt_caba = Entry(ventana, textvariable=var_caballaje)
        txt_caba.pack(pady=5)

        lbl_plazas = Label(ventana, text="Ingresa el no de plazas")
        lbl_plazas.pack(pady=5)
        txt_plazas = Entry(ventana, textvariable=var_plazas)
        txt_plazas.pack(pady=5)

        lbl_eje=Label(ventana,text="Ingresa el eje")
        lbl_eje.pack(pady=5)
        txt_eje=Entry(ventana, textvariable=var_eje)
        txt_eje.pack(pady=5)

        lbl_capacidad=Label(ventana,text="Ingresa la capacidad de carga")
        lbl_capacidad.pack(pady=5)
        txt_capacidad=Entry(ventana, textvariable=var_capacidad)
        txt_capacidad.pack(pady=5)
        btn_actualizar=Button(ventana,text="Actualizar",command=lambda:controlador.Controlador3.cambiar_camiones(var_color.get(),var_marca.get(),var_modelo.get(),var_velocidad.get(),var_caballaje.get(),var_plazas.get(),var_eje.get(),var_capacidad.get(),var_id.get())) 
        btn_actualizar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.cambiar_camiones(ventana,tipo)) 
        btn_volver.pack(pady=5)


    @staticmethod
    def eliminar_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Bienvenido a eliminar camiones"))
        lbl_titulo.pack(pady=5)
        lbl_id=Label(ventana,text=("Ingrese el id del camion a eliminar"))
        lbl_id.pack(pady=5) 
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id)
        txt_id.pack()          
        btn_buscar=Button(ventana,text="buscar", command=lambda:controlador.Controlador3.check_camiones2(ventana,tipo,id.get())) 
        btn_buscar.pack(pady=5) 
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 

    @staticmethod
    def eliminar_camiones2(ventana,tipo,id,color,marca,modelo,velocidad,caballaje,plazas,eje,capacidad):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=("Camion a eliminar:"))
        lbl_titulo.pack(pady=5) 
        filas=""

        
        filas=filas+f"\n ID: {id} -Color: {color} Marca: {marca} Modelo: {modelo}  Velocidad: {velocidad} \nCaballaje: {caballaje} Plazas: {plazas} Eje: {eje} Capacidad: {capacidad} \n"

        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_borrar=Button(ventana,text="Borrar",command=lambda:controlador.Controlador3.eliminar_camiones(id)) 
        btn_borrar.pack(pady=5)
        btn_volver=Button(ventana,text="Regresar", command=lambda:View.menu_acciones(ventana,tipo)) 
        btn_volver.pack(pady=5) 
    