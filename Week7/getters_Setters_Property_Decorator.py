class Cuenta():
    def __init__(self,propietario,saldo,moneda):
        self.__propietario = propietario
        self.__saldo = saldo
        self.__moneda = moneda
        # Getters (metodos GET)
    @property
    def propietario(self):
        return self.__propietario
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def moneda(self):
        return self.__moneda
    
    # Setters (metodos SET)

    @moneda.setter
    def moneda(self,moneda):
        self.__moneda = moneda


cuenta1 = Cuenta('Uriel',200,'pesos')

print(cuenta1.propietario)
print(cuenta1.saldo)
print(cuenta1.moneda)

cuenta1.moneda = 'Euros'
print(cuenta1.moneda)