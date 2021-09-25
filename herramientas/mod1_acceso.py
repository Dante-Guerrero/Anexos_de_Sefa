# Importación externa
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkmb
from PIL import Image,ImageTk
# Importación local
from herramientas import funciones as func
from herramientas import globales as glob
from herramientas import mod3_anexosdesefa as anexosdesefa

########################################################################
class RecuperacionDeContrasena(tk.Toplevel):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""

        self.original_frame = original
        tk.Toplevel.__init__(self)
        self.box_w = 900
        self.box_h = 450
        self.box_sw = self.winfo_screenwidth()
        self.box_sh = self.winfo_screenheight()
        self.box_x = (self.box_sw - self.box_w)/2
        self.box_y = (self.box_sh - self.box_h)/2
        self.geometry('%dx%d+%d+%d' % (self.box_w, self.box_h, self.box_x, self.box_y))
        self.titulo = "Aplicativo: Herramientas de Sefa - versión " + glob.numero_de_version
        self.title(self.titulo)
        self.resizable(False,False)
        self.config(background= glob.color_fondo)

        # Título de la ventana

        self.main_title = Label(self, text="RECUPERACIÓN DE CONTRASEÑA", font=glob.fuente, fg=glob.color_letrasenbotones, bg=glob.color_botones, width="550", height="2")
        self.main_title.pack()

        # Imagen Frame

        self.imagen_email = func.Dar_formato_a_Imagen(100, 100, 'email.png')
        self.imagen_email = ImageTk.PhotoImage(self.imagen_email)
        self.imageframe = tk.Frame(self)
        self.imageframe.config(background= glob.color_fondo)
        self.imageframe.pack()
        
        self.vacio_label1 = Label(self.imageframe, text= "", bg=glob.color_fondo)
        self.imagen_label = Label(self.imageframe, image=self.imagen_email, bg=glob.color_fondo)
        self.vacio_label1.pack()
        self.imagen_label.pack()

        # Contenido Frame

        self.frame = tk.Frame(self)
        self.frame.config(background= glob.color_fondo)
        self.frame.pack()
        
        # Label
        
        self.mensaje = 'Para mantener sus datos de acceso seguros, se enviará su contraseña a su email. Introduzca su dirección y de click al botón "Enviar".'
        self.mensaje_label = Label(self.frame, text=self.mensaje, font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo, wraplength=610)
        self.email_label = Label(self.frame, text="Email:", font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo,  anchor="w", width= "50")
        self.vacio_label1 = Label(self.frame, text= "", bg=glob.color_fondo)
        self.vacio_label2 = Label(self.frame, text= "", bg=glob.color_fondo)
        self.vacio_label3 = Label(self.frame, text= "", bg=glob.color_fondo)
        
        # Entry

        self.email_strg = StringVar()
        self.email_entry = Entry(self.frame, font=glob.fuente, textvariable = self.email_strg, width= "50", borderwidth=2, bg=glob.color_entry)

        # Botones

        self.boton_enviar = Button(self.frame, font=glob.fuente, text="Enviar", command=self.enviar, width="20", height="1", fg=glob.color_letrasenbotones, bg=glob.color_botones, relief="flat", cursor="hand2")
        self.boton_volver = Button(self.frame, font=glob.fuente, text="Volver", command=self.volver, width="20", height="1", fg=glob.color_letrasenbotones, bg=glob.color_botones, relief="flat", cursor="hand2")

        # Ubicaciones

        self.vacio_label1.grid(row=1, column=1, pady= 2, padx=10, columnspan=2)
        self.mensaje_label.grid(row=2, column=1, pady= 2, padx=10, columnspan=2)
        self.vacio_label2.grid(row=3, column=1, pady= 2, padx=10, columnspan=2)
        self.email_label.grid(row=4, column=1, pady= 2, padx=20, columnspan=2)
        self.email_entry.grid(row=5, column=1, pady= 2, padx=10, columnspan=2)
        self.vacio_label3.grid(row=6, column=1, pady= 2, padx=10, columnspan=2)
        self.boton_enviar.grid(row=7, column=1, pady= 2, padx=10)
        self.boton_volver.grid(row=7, column=2, pady= 0, padx=2)

        # Efectos

        func.Efecto_de_boton(self.boton_enviar)
        func.Efecto_de_boton(self.boton_volver)

    #----------------------------------------------------------------------
    def enviar(self):
        """"""
        glob.email = self.email_strg.get()
        if glob.email == "":
            tkmb.showerror("Error", "Falta ingresar el email.", parent=self)
        else:
            func.GoogleSheet_Logueo_Comprobar_email()
            if glob.emails_lista_de_comprobacion != []:
                func.GoogleSheet_Logueo_Comprobar_contrasena()
                func.Enviar_un_email_recordando_clave()
                self.onClose()
            else:
                tkmb.showerror("Error", "El usuario ingresado no existe.", parent=self)

    #----------------------------------------------------------------------
    def volver(self):
        """"""
        self.onClose()
    
    #----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()

########################################################################
class CambioDeContrasena(tk.Toplevel):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""

        self.original_frame = original
        tk.Toplevel.__init__(self)
        self.box_w = 800
        self.box_h = 600
        self.box_sw = self.winfo_screenwidth()
        self.box_sh = self.winfo_screenheight()
        self.box_x = (self.box_sw - self.box_w)/2
        self.box_y = (self.box_sh - self.box_h)/2
        self.geometry('%dx%d+%d+%d' % (self.box_w, self.box_h, self.box_x, self.box_y))
        self.titulo = "Aplicativo: Herramientas de Sefa - versión " + glob.numero_de_version
        self.title(self.titulo)
        self.resizable(False,False)
        self.config(background= glob.color_fondo)

        # Título de la ventana

        self.main_title = Label(self, text="CAMBIO DE CONTRASEÑA", font=("Arial", 14), fg=glob.color_letrasenbotones, bg=glob.color_botones, width="550", height="2")
        self.main_title.pack()

        # Imagen Frame

        self.imagen_password = func.Dar_formato_a_Imagen(100, 100, 'password.png')
        self.imagen_password = ImageTk.PhotoImage(self.imagen_password)
        self.imageframe = tk.Frame(self)
        self.imageframe.config(background= glob.color_fondo)
        self.imageframe.pack()
        
        self.vacio_label1 = Label(self.imageframe, text= "", bg=glob.color_fondo)
        self.imagen_label = Label(self.imageframe, image=self.imagen_password, bg=glob.color_fondo)
        self.vacio_label1.pack()
        self.imagen_label.pack()

        # Contenido Frame

        self.frame = tk.Frame(self)
        self.frame.config(background= glob.color_fondo)
        self.frame.pack()
        
        # Label
        
        self.mensaje = 'Para cambiar su contraseña deberá ingresar sus datos de acceso actuales y la nueva contraseña, que le pediremos confirmar. Después, de click en el botón "Cambiar".'
        self.mensaje_label = Label(self.frame, text=self.mensaje, font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo, wraplength=610)
        self.email_label = Label(self.frame, text="Email:", font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo,  anchor="w", width= "50")
        self.contrasena_label = Label(self.frame, text="Contraseña actual:", font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo,  anchor="w", width= "50")
        self.nueva_contrasena_label = Label(self.frame, text="Nueva contraseña:", font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo,  anchor="w", width= "50")
        self.confirmar_nueva_contrasena_label = Label(self.frame, text="Confirmar nueva contraseña:", font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo,  anchor="w", width= "50")
        self.vacio_label1 = Label(self.frame, text= "", bg=glob.color_fondo)
        self.vacio_label2 = Label(self.frame, text= "", bg=glob.color_fondo)
        self.vacio_label3 = Label(self.frame, text= "", bg=glob.color_fondo)
        
        # Entry

        self.email_strg = StringVar()
        self.email_entry = Entry(self.frame, font=glob.fuente, textvariable = self.email_strg, width= "50", borderwidth=2, bg=glob.color_entry)

        self.contrasena_strg = StringVar()
        self.contrasena_entry = Entry(self.frame, font=glob.fuente, textvariable = self.contrasena_strg, show = "*", width= "50", borderwidth=2, bg=glob.color_entry)

        self.nueva_contrasena_strg = StringVar()
        self.nueva_contrasena_entry = Entry(self.frame, font=glob.fuente, textvariable = self.nueva_contrasena_strg, show = "*", width= "50", borderwidth=2, bg=glob.color_entry)

        self.confirmar_nueva_contrasena_strg = StringVar()
        self.confirmar_nueva_contrasena_entry = Entry(self.frame, font=glob.fuente, textvariable = self.confirmar_nueva_contrasena_strg, show = "*", width= "50", borderwidth=2, bg=glob.color_entry)

        # Botones

        self.boton_cambiar = Button(self.frame, font=glob.fuente, text="Cambiar", command=self.cambiar, width="20", height="1", fg=glob.color_letrasenbotones, bg=glob.color_botones, relief="flat", cursor="hand2")
        self.boton_volver = Button(self.frame, font=glob.fuente, text="Volver", command=self.volver, width="20", height="1", fg=glob.color_letrasenbotones, bg=glob.color_botones, relief="flat", cursor="hand2")

        # Ubicaciones

        self.vacio_label1.grid(row=1, column=1, pady= 2, padx=10, columnspan=2)
        self.mensaje_label.grid(row=2, column=1, pady= 2, padx=10, columnspan=2)
        self.vacio_label2.grid(row=3, column=1, pady= 2, padx=10, columnspan=2)
        self.email_label.grid(row=4, column=1, pady= 2, padx=20, columnspan=2)
        self.email_entry.grid(row=5, column=1, pady= 2, padx=10, columnspan=2)
        self.contrasena_label.grid(row=6, column=1, pady= 2, padx=10, columnspan=2)
        self.contrasena_entry.grid(row=7, column=1, pady= 2, padx=10, columnspan=2)
        self.nueva_contrasena_label.grid(row=8, column=1, pady= 2, padx=10, columnspan=2)
        self.nueva_contrasena_entry.grid(row=9, column=1, pady= 2, padx=10, columnspan=2)
        self.confirmar_nueva_contrasena_label.grid(row=10, column=1, pady= 2, padx=10, columnspan=2)
        self.confirmar_nueva_contrasena_entry.grid(row=11, column=1, pady= 2, padx=10, columnspan=2)
        self.vacio_label3.grid(row=12, column=1, pady= 2, padx=10, columnspan=2)
        self.boton_cambiar.grid(row=13, column=1, pady= 2, padx=10)
        self.boton_volver.grid(row=13, column=2, pady= 0, padx=2)

        # Efectos

        func.Efecto_de_boton(self.boton_cambiar)
        func.Efecto_de_boton(self.boton_volver)

    #----------------------------------------------------------------------
    def cambiar(self):
        """"""
        glob.email = self.email_strg.get()
        glob.contrasena = self.contrasena_strg.get()
        self.nueva_contrasena = self.nueva_contrasena_strg.get()
        self.confirmar_nueva_contrasena = self.confirmar_nueva_contrasena_strg.get()

        if glob.email == "":
            tkmb.showerror("Error", "Falta ingresar el email.", parent=self)
            
        elif glob.contrasena == "":
            tkmb.showerror("Error", "Falta ingresar la contraseña.", parent=self)

        elif self.nueva_contrasena == "":
            tkmb.showerror("Error", "Falta ingresar la nueva contraseña.", parent=self)

        elif self.confirmar_nueva_contrasena == "":
            tkmb.showerror("Error", "Falta confirmar la nueva contraseña.", parent=self)

        else:
            func.GoogleSheet_Logueo_Comprobar_email()
            if glob.emails_lista_de_comprobacion != []:
                func.GoogleSheet_Logueo_Comprobar_contrasena()
                if glob.contrasena == glob.contrasena_apropiada:
                    if self.nueva_contrasena == self.confirmar_nueva_contrasena:
                        glob.contrasena = self.nueva_contrasena
                        func.Cambiar_Contrasena()
                        self.volver()
                    else:
                        tkmb.showerror("Error", 'La nueva contraseña no coincide con la ingresada en el campo "Confirmar nueva contraseña".', parent=self)
                else:
                    tkmb.showerror("Error", "La contraseña ingresada es incorrecta", parent=self)
            else:
                tkmb.showerror("Error", "El usuario ingresado no existe.", parent=self)

    #----------------------------------------------------------------------
    def volver(self):
        """"""
        self.destroy()
        self.original_frame.show()

########################################################################
class Logueo(tk.Toplevel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""

        tk.Toplevel.__init__(self)
        self.box_w = 500
        self.box_h = 500
        self.box_sw = self.winfo_screenwidth()
        self.box_sh = self.winfo_screenheight()
        self.box_x = (self.box_sw - self.box_w)/2
        self.box_y = (self.box_sh - self.box_h)/2
        self.geometry('%dx%d+%d+%d' % (self.box_w, self.box_h, self.box_x, self.box_y))
        self.titulo = "Aplicativo: Herramientas de Sefa - versión " + glob.numero_de_version
        self.title(self.titulo)
        self.resizable(False,False)
        self.config(background= glob.color_fondo)

        # Imagenes Frame

        self.logosefa = func.Dar_formato_a_Imagen(315, 70, 'logosefa.png')
        self.logosefa = ImageTk.PhotoImage(self.logosefa)
        self.herramientas = func.Dar_formato_a_Imagen(240, 50, 'herramientas.png')
        self.herramientas = ImageTk.PhotoImage(self.herramientas)
        self.imageframe = tk.Frame(self)
        self.imageframe.config(background= glob.color_fondo)
        self.imageframe.pack()
        
        self.vacio_label1 = Label(self.imageframe, text= "", bg=glob.color_fondo)
        self.vacio_label2 = Label(self.imageframe, text= "", bg=glob.color_fondo)
        self.vacio_label3 = Label(self.imageframe, text= "", bg=glob.color_fondo)
        self.imagen_label = Label(self.imageframe, image=self.logosefa, bg=glob.color_fondo)
        self.imagen2_label = Label(self.imageframe, image=self.herramientas, bg=glob.color_fondo)

        self.vacio_label1.pack()
        self.imagen_label.pack()
        self.vacio_label2.pack()
        self.imagen2_label.pack()
        self.vacio_label3.pack()

        # Contenido Frame

        self.frame = tk.Frame(self)
        self.frame.config(background= glob.color_fondo)
        self.frame.pack()
        
        # Label
        
        self.email_label = Label(self.frame, text="Email:", font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo,  anchor="w", width= "33")
        self.contrasena_label = Label(self.frame, text="Contraseña:", font= glob.fuente, fg=glob.color_letras, bg=glob.color_fondo, anchor="w", width= "33")
        self.vacio_label1 = Label(self.frame, text= "", bg=glob.color_fondo)
        self.vacio_label2 = Label(self.frame, text= "", bg=glob.color_fondo)
        
        # Entry

        self.email_strg = StringVar()
        self.email_entry = Entry(self.frame, font=glob.fuente, textvariable = self.email_strg, width= "33", borderwidth=2, bg=glob.color_entry)

        self.contrasena_strg = StringVar()
        self.contrasena_entry = Entry(self.frame, font=glob.fuente, textvariable = self.contrasena_strg, show="*", width= "33", borderwidth=2, bg=glob.color_entry)

        # Botones

        self.boton_ingresar = Button(self.frame, font=glob.fuente, text="Ingresar", command=self.intentar_ingresar, width="20", height="1", fg=glob.color_letrasenbotones, bg=glob.color_botones, relief="flat", cursor="hand2")
        self.boton_olvido = Button(self.frame, font=glob.fuente_pequeña, text="Olvidé mi contraseña", command=self.recuperar_contrasena, width="25", height="1", fg=glob.color_botones, bg=glob.color_fondo, relief="flat", cursor="hand2")
        self.boton_cambio = Button(self.frame, font=glob.fuente_pequeña, text="Deseo cambiar de contraseña", command=self.cambiar_contrasena, width="25", height="1", fg=glob.color_botones, bg=glob.color_fondo, relief="flat", cursor="hand2")

        # Ubicaciones

        self.email_label.grid(row=1, column=1, pady= 2, padx=20)
        self.email_entry.grid(row=2, column=1, pady= 2, padx=10)
        self.contrasena_label.grid(row=3, column=1, pady= 2, padx=10)
        self.contrasena_entry.grid(row=4, column=1, pady= 2, padx=10)
        self.vacio_label1.grid(row=5, column=1, pady= 2, padx=10)
        self.boton_ingresar.grid(row=6, column=1, pady= 2, padx=10)
        self.vacio_label2.grid(row=7, column=1, pady= 2, padx=10)
        self.boton_olvido.grid(row=8, column=1, pady= 0, padx=2)
        self.boton_cambio.grid(row=9, column=1, pady= 0, padx=2)

        # Efectos

        func.Efecto_de_boton(self.boton_ingresar)

    #----------------------------------------------------------------------
    def intentar_ingresar(self):
        """"""

        glob.email = self.email_strg.get()
        glob.contrasena = self.contrasena_strg.get()

        if glob.email == "":
            tkmb.showerror("Error", "Falta ingresar el email.", parent=self)
            
        elif glob.contrasena == "":
            tkmb.showerror("Error", "Falta ingresar la contraseña.", parent=self)

        else:
            func.GoogleSheet_Logueo_Comprobar_email()
            if glob.emails_lista_de_comprobacion != []:
                func.GoogleSheet_Logueo_Comprobar_contrasena()
                if glob.contrasena == glob.contrasena_apropiada:
                    func.GoogleSheet_Logueo_Establecer_usuario()
                    self.withdraw()
                    subFrame = anexosdesefa.MyApp(self)
                else:
                    tkmb.showerror("Error", "La contraseña ingresada es incorrecta", parent=self)
            else:
                tkmb.showerror("Error", "El usuario ingresado no existe.", parent=self)
    
    #----------------------------------------------------------------------
    def recuperar_contrasena(self):
        """"""
        self.withdraw()
        subFrame = RecuperacionDeContrasena(self)

    #----------------------------------------------------------------------
    def cambiar_contrasena(self):
        """"""
        self.withdraw()
        subFrame = CambioDeContrasena(self)

    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.update()
        self.deiconify()
