class jugadores:
    def __format__ (self, formato):
        if formato ==  "Equipo":
            return f"El Equipo es {self.Equipo}"
        return str(self)    
    def __init__(self, Nombre, Numero, Equipo):
        self.Nombre = Nombre
        self.Numero = Numero
        self.Equipo = Equipo
    def __str__ (self):
        return f"El Jugador es {self.Nombre} y su numero es {self.Numero} y juega en el equipo {self.Equipo}"
    def __repr__ (self):
        return f"Nombre = {self.Nombre}, Numero = {self.Numero}, Equipo = {self.Equipo}"
print("Ingresa los datos del jugador")
nombre = input("Nombre: ")
numero = input("Numero: ")
equipo = input("Equipo: ")
jugador1 = jugadores(nombre, numero, equipo)
Diccionariojugador = {"Nombre": jugador1.Nombre, "Numero": jugador1.Numero, "Equipo": jugador1.Equipo}
print(jugador1)
print(Diccionariojugador)