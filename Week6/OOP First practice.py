class Coche():
    largo = 250
    ancho = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self): #Este metodo trata de cambiar la propiedad en marcha
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'
        
micoche=Coche()

print(f'El largo de coche es de {micoche.largo}')
print(f'El coche tiene {micoche.ruedas} ruedas')

micoche.arrancar() #Estamos llamando al metodo arrancar

print(micoche.estado())

print("------------------------Creemos un segundo objeto ----------------------------------")

micoche2 = Coche()

print(f'El largo de coche es de {micoche.largo}')
print(f'El coche tiene {micoche.ruedas} ruedas')

print(micoche2.estado())