from pytube import YouTube
from pytube.exceptions import RegexMatchError
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class YouTubeDownloader:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("YouTube Downloader")
        self.ventana.resizable = False
        self.url = StringVar()
        self.directorio_texto = StringVar()
        self.directorio_texto.set('Directorio:')
        self.crear_interfaz()
        self.ventana.mainloop()

    def cambiar_directorio(self):
        self.directorio_texto.set(filedialog.askdirectory())

    def crear_interfaz(self):
        self.ventana.config(bg="black")
        directorio = Label(self.ventana)
        directorio.config(textvariable=self.directorio_texto,
                          font=("Verdana", 14), fg="red", bg="black")
        directorio.grid(column=0, row=0, columnspan=2, pady=7)
        boton_directorio = Button(
            self.ventana, text="Buscar directorio", command=self.cambiar_directorio)
        boton_directorio.grid(column=2, row=0, columnspan=2, pady=7)
        info = Label(
            self.ventana, text="Inserte el link del video a descargar")
        info.grid(column=0, row=2, columnspan=2)
        info.config(font=("Verdana", 14), fg="red", bg="black")
        texto = Entry(self.ventana, textvariable=self.url)
        texto.grid(column=0, row=3, columnspan=2, pady=7, ipadx=100)
        boton_descarga = Button(
            self.ventana, text="Descargar", command=self.descargar)
        boton_descarga.config(bg='red', fg='black')
        boton_directorio.config(bg='red', fg='black')
        boton_descarga.grid(column=2, row=3, columnspan=2, pady=7)

    def descargar(self):
        if self.directorio_texto.get() == 'Directorio:' or not self.url.get():
            messagebox.showinfo('Atención', "Complete los campos faltantes!")
        else:
            try:
                youtube = YouTube(self.url.get())
                youtube.streams.get_highest_resolution().download(self.directorio_texto.get())
                messagebox.showinfo(
                    'Atención!', 'El video fue descargado existosamente')
            except RegexMatchError:
                messagebox.showinfo(
                    '¡Error!', 'El link ingresado no es válido')


i = YouTubeDownloader()
