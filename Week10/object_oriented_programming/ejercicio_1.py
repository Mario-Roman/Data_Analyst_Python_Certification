'''Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.

mostrar(): Muestra los datos de la persona.

esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad'''

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        if len(dni) == 9:
            self.__dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)

    def esMayorDeEdad(self):
        return self.__edad >= 18


# Crear una instancia de la clase Persona
persona = Persona()

# Establecer los atributos utilizando los setters
persona.set_nombre("Mario")
persona.set_edad(27)
persona.set_dni("123456789")

# Obtener los atributos utilizando los getters
nombre = persona.get_nombre()
edad = persona.get_edad()
dni = persona.get_dni()

# Mostrar los datos de la persona
persona.mostrar()

# Verificar si la persona es mayor de edad
if persona.esMayorDeEdad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
