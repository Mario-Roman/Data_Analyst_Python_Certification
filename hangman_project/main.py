import random
from palabras import palabras
from ahorcado_diagramas import diagramas

class Ahorcado:
    def __init__(self):
        self.palabra = self.obtener_palabra_aleatoria()
        self.intentos = 0
        self.letras_adivinadas = []
    
    def obtener_palabra_aleatoria(self):
        return random.choice(palabras)
    
    def mostrar_palabra(self):
        palabra_mostrada = ""
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
        return palabra_mostrada.strip()
    
    def adivinar_letra(self, letra):
        if letra in self.palabra:
            self.letras_adivinadas.append(letra)
        else:
            self.intentos += 1
    
    def adivinar_palabra(self, palabra):
        if palabra == self.palabra:
            self.letras_adivinadas = list(palabra)
        else:
            self.intentos += 1
    
    def dibujar_ahorcado(self):
        return diagramas[self.intentos]
    
    def jugar(self):
        print("Bienvenido al juego del Ahorcado!")
        print("Categoría: Cine")
        print("Palabra a adivinar:", self.mostrar_palabra())
        
        while self.intentos < len(diagramas) - 1:
            letra = input("Ingresa una letra: ")
            self.adivinar_letra(letra)
            
            print("Palabra a adivinar:", self.mostrar_palabra())
            print(self.dibujar_ahorcado())
            
            if "_" not in self.mostrar_palabra():
                print("¡Felicidades! Has adivinado la palabra correctamente.")
                break
        
        if "_" in self.mostrar_palabra():
            print("Perdiste!. La palabra correcta era:", self.palabra)
    
ahorcado = Ahorcado()
ahorcado.jugar()
