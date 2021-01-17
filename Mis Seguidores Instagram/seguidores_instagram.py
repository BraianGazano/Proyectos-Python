from instascrape import *
from tkinter import *
from tkinter import messagebox
import time


class DatosInstagram:

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title("Mis datos Instagram")
        self.ventana.iconbitmap(
            "Mis Seguidores Instagram\icons\instagram-logo.ico")
        self.busqueda_usuario = StringVar()
        self.crear_interfaz()
        self.ventana.resizable(width=False, height=False)
        self.ventana.mainloop()

    def crear_interfaz(self):
        self.ventana.config(bg="#DD2A7B")
        info = Label(
            self.ventana, text="Inserte el usuario de Instagram")
        info.grid(column=0, row=0, columnspan=3)
        info.config(font=("Arial", 15, "bold"), fg="orange", bg="#DD2A7B")

        texto = Entry(self.ventana, textvariable=self.busqueda_usuario)
        texto.config(borderwidth='2')
        texto.grid(column=0, row=1, columnspan=2, ipadx=50, padx=3)

        boton_busqueda = Button(
            self.ventana, text="Buscar", command=self.buscar)
        boton_busqueda.config(borderwidth='2', bg="orange",
                              font=("Arial", 11, "bold"), fg="#DD2A7B")
        boton_busqueda.grid(column=2, row=1, pady=1)

    def normalizar_busqueda(self, busqueda):
        return busqueda.lower()

    def buscar(self):
        usuario = self.normalizar_busqueda(self.busqueda_usuario.get())
        if not usuario:
            messagebox.showinfo(
                'Atención', "Por favor, ingrese el nombre del usuario!")
        else:
            perfil = Profile("https://www.instagram.com/"+usuario)
            perfil.scrape()
            messagebox.showinfo(
                'Datos obtenidos exitosamente!', 'Usuario Hackeado: '+usuario + "\n"+"Seguidores: " + str(perfil.followers)+"\n" + "Publicaciones: " + str(perfil.posts) + "\n" + "Seguidos: " + str(perfil.following))


i = DatosInstagram()
