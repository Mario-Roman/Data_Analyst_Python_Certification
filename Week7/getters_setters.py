class Cuenta():
    def __init__(self,propietario,saldo,moneda):
        self.__propietario = propietario
        self.__saldo = saldo
        self.__moneda = moneda
        # Getters (metodos GET)
    def get_Propietario(self):
        return self.__propietario
    
    def get_Saldo(self):
        return self.__saldo
    
    def get_Moneda(self):
        return self.__moneda
    
        # Setters (metodos SET)

    def set_moneda(self,moneda):
        self.__moneda = moneda


cuenta1 = Cuenta('Uriel',200,'pesos')

#print(cuenta1.__saldo) #Observa que pasa si ejecutas esta sentencia

print(cuenta1.get_Saldo())
print(cuenta1.get_Moneda())

cuenta1.set_moneda('Dolares')
print(cuenta1.get_Moneda())
