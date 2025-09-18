class SENA:
    def __new__ (cls, nombre, edad):
        return super().__new__(cls)        


    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__ (self):
        print("Objeto eliminado")