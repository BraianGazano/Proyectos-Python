from pygame import mixer
import pygame
import PySimpleGUI
from threading import Thread
import os


class ReproductorMP3:

    def __init__(self):

        PySimpleGUI.theme("DarkGreen7")
        layout = [
            [PySimpleGUI.Button(button_text="Elegir carpeta", key="carpeta", size=(16, 1)), PySimpleGUI.Button(
                button_text="Elegir canción", size=(16, 1),  key="cancion")],
            [PySimpleGUI.Image(
                filename=r'Reproductor de Musica\mp3-player.png', key="-image-")],
            [PySimpleGUI.Text("-----------Nombre-----------",
                              key="nombre", justification=("center"), font='Courier 12', text_color='yellow', background_color='green')],
            [PySimpleGUI.Button("<<", size=(10, 1)), PySimpleGUI.Button(
                button_text="||", key="pausa", size=(10, 1)), PySimpleGUI.Button(">>", size=(10, 1))]
        ]
        self.ventana = PySimpleGUI.Window('Reproductor MP3',
                                          layout,
                                          no_titlebar=False,
                                          location=(0, 0))
        self.boton_pausa = self.ventana["pausa"]
        self.nombre_cancion = self.ventana["nombre"]
        self.reset_configuracion()
        self.posicion_lista = 0
        self.pausa = False
        self.proceso = ""

    def reset_configuracion(self):
        self.ruta = ""
        self.lista_canciones = []
        self.estado = False

    def iniciar(self):
        try:
            while True:
                evento, valores = self.ventana.read(timeout=0)
                if evento == "carpeta":
                    self.reset_configuracion()
                    self.ruta = PySimpleGUI.popup_get_folder(
                        title="Seleccionar carpeta", message="Carpeta seleccionada")
                    for archivo in os.listdir(self.ruta):
                        if archivo.endswith(".mp3"):
                            self.lista_canciones.append(archivo)
                    if len(self.lista_canciones) == 0:
                        pass
                    else:
                        self.nombre_cancion.update(self.lista_canciones[0])
                        self.cargar_cancion(self.ruta, self.lista_canciones[0])
                elif evento == "cancion":
                    self.reset_configuracion()
                    self.ruta = PySimpleGUI.popup_get_file(title="Seleccionar canción", message="Canción seleccionada", file_types=(
                        ("MP3 Files", "*.mp3"), ("OGG Files", "*.ogg"),))
                    self.cargar_cancion_unica(self.ruta)
                    self.nombre_cancion.update(self.ruta.split("/")[-1])
                elif evento == ">>":
                    self.posicion_lista += 1
                    self.estado = False
                    self.nombre_cancion.update(
                        self.lista_canciones[self.posicion_lista])
                    self.cargar_cancion(
                        self.ruta, self.lista_canciones[self.posicion_lista])
                elif evento == "<<":
                    if self.posicion_lista >= 0:
                        self.posicion_lista -= 1
                    self.estado = False
                    self.nombre_cancion.update(
                        self.lista_canciones[self.posicion_lista])
                    self.cargar_cancion(
                        self.ruta, self.lista_canciones[self.posicion_lista])

                elif evento == "pausa":
                    if not self.pausa:
                        self.boton_pausa.update(text="|>")
                        self.proceso = "pausa"
                        self.pausa = True
                    else:
                        self.boton_pausa.update(text="||")
                        self.proceso = "continuar"
                        self.pausa = False
                else:
                    pass
                if evento in ("Exit", None):
                    break
        except IndexError:
            PySimpleGUI.Popup('Ups!', 'No hay canciones en la lista!')
            self.iniciar()

    def cargar_cancion(self, ruta, cancion):
        hilo = Thread(target=self.reproducir, args=(
            ruta+"/"+cancion,), daemon=True)
        hilo.start()

    def cargar_cancion_unica(self, ruta):
        hilo = Thread(target=self.reproducir, args=(ruta,), daemon=True)
        hilo.start()

    def reproducir(self, ruta):
        self.estado = True

        try:
            mixer.init()
            mixer.music.load(ruta)
            mixer.music.set_volume(0.7)
            mixer.music.play()
            while True:
                if not self.estado:
                    break
                elif self.proceso == "pausa":
                    mixer.music.pause()
                    self.proceso = ""
                elif self.proceso == "continuar":
                    mixer.music.unpause()
                    self.proceso = ""
        except pygame.error:
            pass


ReproductorMP3().iniciar()
