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

    def setear_operacion(self, dato, escritura):
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

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")

    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

    def crear_interfaz(self):

        boton_0 = Button(self.ventana, text="0",
                         command=lambda: self.setear_operacion("0", True))
        boton_1 = Button(self.ventana, text="1",
                         command=lambda: self.setear_operacion("1", True))
        boton_2 = Button(self.ventana, text="2",
                         command=lambda: self.setear_operacion("2", True))
        boton_3 = Button(self.ventana, text="3",
                         command=lambda: self.setear_operacion("3", True))
        boton_4 = Button(self.ventana, text="4",
                         command=lambda: self.setear_operacion("4", True))
        boton_5 = Button(self.ventana, text="5",
                         command=lambda: self.setear_operacion("5", True))
        boton_6 = Button(self.ventana, text="6",
                         command=lambda: self.setear_operacion("6", True))
        boton_7 = Button(self.ventana, text="7",
                         command=lambda: self.setear_operacion("7", True))
        boton_8 = Button(self.ventana, text="8",
                         command=lambda: self.setear_operacion("8", True))
        boton_9 = Button(self.ventana, text="9",
                         command=lambda: self.setear_operacion("9", True))
        boton_suma = Button(self.ventana, text="+",
                            command=lambda: self.setear_operacion("+", True))
        boton_resta = Button(self.ventana, text="-",
                             command=lambda: self.setear_operacion("-", True))
        boton_multiplicacion = Button(
            self.ventana, text="*", command=lambda: self.setear_operacion("*", True))
        boton_division = Button(
            self.ventana, text="/", command=lambda: self.setear_operacion("/", True))
        boton_igual = Button(self.ventana, text="=",
                             command=lambda: self.setear_operacion("=", False))
        boton_borrar = Button(self.ventana, text="\u232B",
                              command=lambda: self.setear_operacion("\u232B", False))
        boton_reiniciar = Button(
            self.ventana, text="C", command=lambda: self.setear_operacion("C", False))
        boton_punto = Button(
            self.ventana, text=".", command=lambda: self.setear_operacion(".", True))
        boton_1.grid(column=0, row=2, pady=7)
        boton_2.grid(column=1, row=2)
        boton_3.grid(column=2, row=2)
        boton_4.grid(column=0, row=3, pady=7)
        boton_5.grid(column=1, row=3)
        boton_6.grid(column=2, row=3)
        boton_7.grid(column=0, row=4, pady=7)
        boton_8.grid(column=1, row=4)
        boton_9.grid(column=2, row=4)
        boton_0.grid(column=1, row=5)
        boton_reiniciar.grid(column=2, row=5)
        boton_punto.grid(column=0, row=5)
        boton_borrar.grid(column=4, row=2, pady=7)
        boton_suma.grid(column=4, row=3, pady=7)
        boton_resta.grid(column=4, row=4, pady=7)
        boton_multiplicacion.grid(column=4, row=5, pady=7)
        boton_division.grid(column=4, row=6, pady=7)
        boton_igual.grid(column=0, row=6, columnspan=3)
        boton_igual.config(width=20)
        boton_division.config(width=6)
        boton_multiplicacion.config(width=6)
        boton_resta.config(width=6)
        boton_suma.config(width=6)
        boton_borrar.config(width=6)
        boton_0.config(width=3)
        boton_1.config(width=3)
        boton_2.config(width=3)
        boton_3.config(width=3)
        boton_4.config(width=3)
        boton_5.config(width=3)
        boton_6.config(width=3)
        boton_7.config(width=3)
        boton_8.config(width=3)
        boton_9.config(width=3)
        boton_punto.config(width=3)
        boton_reiniciar.config(width=3)
        self.pantalla = Text(self.ventana, state="disabled", width=20, height=3,
                             background="#D6C30F", foreground="white", font=("Arial", 17))
        self.pantalla.grid(column=0, row=0, columnspan=5)


i = Calculadora()
