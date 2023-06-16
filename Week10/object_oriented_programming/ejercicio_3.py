'''Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye los siguientes métodos para la clase:

Un constructor.

Los setters y getters para el nuevo atributo.

En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad; por lo tanto hay que crear un método es TitularVálido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

Además la retirada de dinero sólo se podrá hacer si el titular es válido.

El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

Piensa los métodos heredados de la clase madre que hay que reescribir.'''

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        return print(f"Cuenta - Titular: {self.titular}, Cantidad: {self.cantidad}")


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def es_titular_valido(self):
        return self.titular.edad >= 18 and self.titular.edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para realizar la retirada.")

    def mostrar(self):
        return print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%")

cuenta = CuentaJoven('Mario', 1500, 15  )
cuenta.mostrar()