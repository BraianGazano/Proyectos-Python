from tkinter import *
from tkinter import messagebox


class Calculadora():

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title("Calculadora")
        self.ventana.resizable(False, False)
        self.operacion = ""
        self.crear_interfaz()
        self.bloqueo_teclado = False
        self.ventana.mainloop()

    """
    @param dato: Caracter correspondiente al boton que fue presionado
    @param escritura: Dependiendo de si es True o False el caracter será enviado escrito en pantalla o no.

    En base al boton presionado se realizara la operacion seleccionada.
    """

    def evento_click(self, dato, escritura):
        try:
            if not escritura:
                if self.bloqueo_teclado and dato == "\u232B":
                    self.operacion = ""
                    self.limpiarPantalla()
                    self.bloqueo_teclado = False
                elif dato == "=" and self.operacion != "":
                    self.limpiarPantalla()
                    self.operacion = str(eval(self.operacion))
                    self.mostrarEnPantalla(str(self.operacion))
                    self.bloqueo_teclado = True
                elif dato == "\u232B" and self.operacion != "":
                    self.operacion = str(
                        self.operacion[:len(self.operacion)-1])
                    self.limpiarPantalla()
                    self.mostrarEnPantalla(self.operacion)
                elif dato == "C" and self.operacion != "":
                    self.limpiarPantalla()
                    self.operacion = ""
            else:
                self.operacion += str(dato)
                self.mostrarEnPantalla(dato)
        except ZeroDivisionError:
            messagebox.showinfo(
                'Atención!', 'No se puede realizar la división por 0')
            self.operacion = ""
        except SyntaxError:
            messagebox.showinfo(
                'Atención!', 'La expresión no se encuentra escrita correctamente')
            self.operacion = ""

    """
    @param valor: Dato a mostrar en pantalla
    """

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")

    """
    Elimina todos los caracteres que se encuentren en pantalla
    """

    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

    """
    @param botones: Lista con todos los botones de la interfaz
    """

    def completar_grilla(self, botones):
        contador = 0
        for fila in range(1, 5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                botones[contador].config(width=6)
                contador += 1
        botones[17].grid(column=3, row=6)
        botones[16].config(width=20)
        botones[16].grid(column=0, row=6, columnspan=3)
        botones[17].config(width=6)

    def crear_interfaz(self):

        boton_0 = Button(self.ventana, text="0",
                         command=lambda: self.evento_click("0", True))
        boton_1 = Button(self.ventana, text="1",
                         command=lambda: self.evento_click("1", True))
        boton_2 = Button(self.ventana, text="2",
                         command=lambda: self.evento_click("2", True))
        boton_3 = Button(self.ventana, text="3",
                         command=lambda: self.evento_click("3", True))
        boton_4 = Button(self.ventana, text="4",
                         command=lambda: self.evento_click("4", True))
        boton_5 = Button(self.ventana, text="5",
                         command=lambda: self.evento_click("5", True))
        boton_6 = Button(self.ventana, text="6",
                         command=lambda: self.evento_click("6", True))
        boton_7 = Button(self.ventana, text="7",
                         command=lambda: self.evento_click("7", True))
        boton_8 = Button(self.ventana, text="8",
                         command=lambda: self.evento_click("8", True))
        boton_9 = Button(self.ventana, text="9",
                         command=lambda: self.evento_click("9", True))
        boton_suma = Button(self.ventana, text="+",
                            command=lambda: self.evento_click("+", True))
        boton_resta = Button(self.ventana, text="-",
                             command=lambda: self.evento_click("-", True))
        boton_multiplicacion = Button(
            self.ventana, text="*", command=lambda: self.evento_click("*", True))
        boton_division = Button(self.ventana, text="/",
                                command=lambda: self.evento_click("/", True))
        boton_punto = Button(self.ventana, text=".",
                             command=lambda: self.evento_click(".", True))
        boton_igual = Button(self.ventana, text="=",
                             command=lambda: self.evento_click("=", False))
        boton_borrar = Button(self.ventana, text="\u232B",
                              command=lambda: self.evento_click("\u232B", False))
        boton_reiniciar = Button(
            self.ventana, text="C", command=lambda: self.evento_click("C", False))

        botones = [boton_1, boton_2, boton_3, boton_borrar, boton_4, boton_5, boton_6, boton_suma, boton_7, boton_8, boton_9,
                   boton_resta, boton_punto, boton_0, boton_reiniciar, boton_multiplicacion, boton_igual, boton_division]
        self.completar_grilla(botones)

        self.pantalla = Text(self.ventana, state="disabled", width=20, height=3,
                             background="#D6C30F", foreground="white", font=("Arial", 17))
        self.pantalla.grid(column=0, row=0, columnspan=5)


i = Calculadora()
