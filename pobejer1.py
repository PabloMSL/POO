class Personas:
    def __init__ (self, tez, nombre, edad, numerodocumento):
        self.tez = tez
        self.nombre = nombre
        self.edad = edad
        self.numerodocumento = numerodocumento
persona1 = Personas("morena", "Juan", 20, "123456789")
print(persona1.tez, persona1.nombre, persona1.edad, persona1.numerodocumento)