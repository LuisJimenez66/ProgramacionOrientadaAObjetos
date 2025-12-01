from tkinter import *
from tkinter import messagebox
from controller import controlador1, controlador2
from model import nota
class View():
    def __init__(self,ventana):
        ventana.title("...::Notas system::...")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def menu_principal (ventana):
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text="..::Menu Principal::..")
        lbl1.pack(pady=10)
        btn_registro=Button(ventana, width=40,justify=CENTER,text=("1.-Registro"), command=lambda: View.registro(ventana))
        btn_registro.pack(pady=15)    
        btn_login=Button(ventana, width=40,justify=CENTER,text=("2.-Login"), command=lambda: View.login(ventana))
        btn_login.pack(pady=15)  
        btn_salir=Button(ventana, width=40,justify=CENTER,text=("3.-Salir"), command=ventana.quit)
        btn_salir.pack(pady=15)  


    @staticmethod
    def borrar_pantalla(ventana):
        for i in ventana.winfo_children():
            i.destroy()

    @staticmethod
    def registro(ventana):
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text="..::Registro en el sistema::..",justify=CENTER)
        lbl1.pack(pady=10)
        #Nombre
        lbl_nombre=Label(ventana,text="¿Cual es tu nombre?", justify= CENTER)
        lbl_nombre.pack(pady=10)
        txt_nombre=Entry(ventana)
        txt_nombre.focus()
        txt_nombre.pack(pady=10)
        #Apellidos
        lbl_apellidos=Label(ventana,text="¿Cuales son tus apellidos?", justify= CENTER)
        lbl_apellidos.pack(pady=10)
        txt_apellidos=Entry(ventana)
        txt_apellidos.pack(pady=10)
        #Email
        lbl_email=Label(ventana,text="Ingresa tu email", justify= CENTER)
        lbl_email.pack(pady=10)
        txt_email=Entry(ventana)
        txt_email.pack(pady=10)
        #Contraseña
        lbl_pass=Label(ventana,text="Ingresa tu contraseña", justify= CENTER)
        lbl_pass.pack(pady=10)
        txt_pass=Entry(ventana, show="*")
        txt_pass.pack(pady=10)
        #Botones
        btn_registrar=Button(ventana,text="Registrar", command=lambda:controlador1.Controlador.registro(txt_nombre.get(),txt_apellidos.get(),txt_email.get(),txt_pass.get(),ventana))
        btn_registrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver", command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def login(ventana):
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text="..::Inicio de sesion::..",justify=CENTER)
        lbl1.pack(pady=10)
        #email
        lbl_email=Label(ventana,text="Ingresa tu email", justify= CENTER)
        lbl_email.pack(pady=10)
        txt_email=Entry(ventana)
        txt_email.focus()
        txt_email.pack(pady=10)
        #contraseña
        lbl_pass=Label(ventana,text="Ingresa tu contraseña", justify= CENTER)
        lbl_pass.pack(pady=10)
        txt_pass=Entry(ventana, show="*")
        txt_pass.pack(pady=10)
        #Botones
        btn_registrar=Button(ventana,text="Entrar", command=lambda:controlador1.Controlador.login(txt_email.get(),txt_pass.get(),ventana))
        btn_registrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver", command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=10)    

    @staticmethod
    def Entrar(ventana,id_usuario,nombre,apellido):
        global id_user,nom_user,ape_user
        id_user=id_usuario
        nom_user=nombre
        ape_user=apellido
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text=f"..::Bienvenido {nombre} {apellido}::..",justify=CENTER)
        lbl1.pack(pady=10)
        #Botones
            #Boton Crear
        btn_crear=Button(ventana,text="1.-Crear", command=lambda:View.crear(ventana,id_usuario,nombre,apellido))
        btn_crear.pack(pady=10)
            #Boton Mostrar
        btn_mostrar=Button(ventana,text="2.-Mostrar", command=lambda:View.mostrar(ventana,id_usuario,nombre,apellido))
        btn_mostrar.pack(pady=10)
            #Boton Cambiar
        btn_cambiar=Button(ventana,text="3.-Cambiar", command=lambda:View.cambiar(ventana,id_usuario,nombre,apellido))
        btn_cambiar.pack(pady=10)
            #Boton Eliminar
        btn_eliminar=Button(ventana,text="4.-Eliminar", command=lambda:View.eliminar(ventana,id_usuario,nombre,apellido))
        btn_eliminar.pack(pady=10)
            #Boton regresar
        btn_volver=Button(ventana,text="5.-Regresar", command=lambda:View.login(ventana))
        btn_volver.pack(pady=10)   


    @staticmethod
    def crear(ventana,id_usuario,nombre,apellido):
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text=f"..:: {nombre} {apellido} vamos a crear Nota::..",justify=CENTER)
        lbl1.pack(pady=10)
        #titulo
        lbl_titulo=Label(ventana,text="Titulo:", justify= CENTER)
        lbl_titulo.pack(pady=10)
        txt_titulo=Entry(ventana)
        txt_titulo.focus()
        txt_titulo.pack(pady=10)
        #descripcion
        lbl_desc=Label(ventana,text="Descripción:", justify= CENTER)
        lbl_desc.pack(pady=10)
        txt_desc=Entry(ventana)
        txt_desc.pack(pady=10)
        #Botones
        btn_registrar=Button(ventana,text="Guardar", command=lambda:controlador2.ControladorNotas.insertar(id_usuario,txt_titulo.get(),txt_desc.get()))
        btn_registrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver", command=lambda:View.Entrar(ventana,id_usuario,nombre,apellido))
        btn_volver.pack(pady=10)     


    @staticmethod
    def mostrar(ventana,id_usuario,nombre,apellido):
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text=f"..::{nombre} {apellido} Tus notas son::..",justify=CENTER)
        lbl1.pack(pady=10)
        #Mostrar
        filas=""
        registros=nota.Nota.mostrar(id_usuario)
        num_nota=1
        if len(registros)>=1:
            for i in registros:
                filas=filas+f"\nNota: {num_nota} \n ID: {i[0]} -Titulo: {i[2]} Fecha de cracion: {i[4]}\n Descripcion: {i[3]}\n"
                num_nota=num_nota+1
        else:
            messagebox.showinfo(icon=Warning, message="...No existen notas para este usuario...")
        #Botones
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)
        btn_volver=Button(ventana,text="Volver", command=lambda:View.Entrar(ventana,id_usuario,nombre,apellido))
        btn_volver.pack(pady=10)      

    @staticmethod
    def cambiar(ventana,id_usuario,nombre,apellido):
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text=f"..:: {nombre} {apellido} Vamos a modificar una nota::..",justify=CENTER)
        lbl1.pack(pady=10)
        #Ingresar ID
        lbl_idnota=Label(ventana,text="ID de la nota a cambiar:", justify= CENTER)
        lbl_idnota.pack(pady=10)
        txt_idnota=Entry(ventana)
        txt_idnota.focus()
        txt_idnota.pack(pady=10)
        #Titulo
        lbl_titulo=Label(ventana,text="Nuevo titulo", justify= CENTER)
        lbl_titulo.pack(pady=10)
        txt_titulo=Entry(ventana)
        txt_titulo.pack(pady=10)
        #Descripcion
        lbl_desc=Label(ventana,text="Nueva Descripcion", justify= CENTER)
        lbl_desc.pack(pady=10)
        txt_desc=Entry(ventana)
        txt_desc.pack(pady=10)
        #Botones
        btn_registrar=Button(ventana,text="Guardar",command=lambda:controlador2.ControladorNotas.cambiar(txt_idnota.get(),txt_titulo.get(),txt_desc.get()))
        btn_registrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver", command=lambda:View.Entrar(ventana,id_usuario,nombre,apellido))
        btn_volver.pack(pady=10)


    @staticmethod
    def eliminar(ventana,id_usuario,nombre,apellido):
        View.borrar_pantalla(ventana)
        lbl1=Label(ventana,text=f"..:: {nombre} {apellido} Vamos a Eliminar una Nota::..",justify=CENTER)
        lbl1.pack(pady=10)
        #Id eliminar
        lbl_idnota=Label(ventana,text="ID de la nota a eliminar", justify=CENTER)
        lbl_idnota.pack(pady=10)
        txt_idnota=Entry(ventana)
        txt_idnota.focus()
        txt_idnota.pack(pady=10)
        #Botones
        btn_eliminar=Button(ventana, text="Eliminar", command=lambda:controlador2.ControladorNotas.eliminar(txt_idnota.get()))
        btn_eliminar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver", command=lambda:View.Entrar(ventana,id_usuario,nombre,apellido))
        btn_volver.pack(pady=10)          






    


