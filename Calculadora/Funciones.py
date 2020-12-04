class Funciones:

    def sumar(self, a, b):
        return a+b

    def restar(self, a, b):
        return a-b

    def multiplicar(self, a, b):
        return a*b

    def dividir(self, a, b):
        try:
            return a/b
        except ArithmeticError:
            print("No se puede dividir por cero")
