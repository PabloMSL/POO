class Alumnos:
    def __init__ (self, Nota1, Nota2, Nombre, Salon):
        self.Nota1 = Nota1
        self.Nota2 = Nota2
        self.Nombre = Nombre
        self.Salon = Salon
alumno1 = Alumnos(4, 5, "Juan", "202")
print(alumno1.Nota1, alumno1.Nota2, alumno1.Nombre, alumno1.Salon)