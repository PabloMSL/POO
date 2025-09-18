class Colegio:
    def __format__ (self, formato):
        if formato ==  "Horario":
            return f"El Horario es {self.Horario}"
        return str(self)    
    def __init__(self, Horario, Nombre, Grado, Cantidad, Profesor, Materia):
        self.Horario = Horario
        self.Nombre = Nombre
        self.Grado = Grado
        self.Cantidad = Cantidad
        self.Profesor = Profesor
        self.Materia = Materia
    def __str__ (self):
        return f"El {self.Nombre} del grado {self.Grado} tiene la materia de {self.Materia} con el profesor {self.Profesor}"
    def __repr__ (self):
        return f"Nombre = {self.Nombre}, Grado = {self.Grado}, Materia = {self.Materia}"
print("Ingresa los datos del colegio")
horario = input("Horario: ")
nombre = input("Nombre: ")
grado = input("Grado: ")
cantidad = int(input("Cantidad de estudiantes: "))
profesor = input("Profesor: ")
materia = input("Materia: ")
colegio1 = Colegio(horario, nombre, grado, cantidad, profesor, materia)
print("Ingresa los datos de otro colegio")
horario = input("Horario: ")
nombre = input("Nombre: ")
grado = input("Grado: ")
cantidad = int(input("Cantidad de estudiantes: "))
profesor = input("Profesor: ")
materia = input("Materia: ")
colegio2 = Colegio(horario, nombre, grado, cantidad, profesor, materia)
DiccionarioProfesores = {"Colegio1": {"Profesor": colegio1.Profesor, "Materia": colegio1.Materia}, "Colegio2": {"Profesor": colegio2.Profesor, "Materia": colegio2.Materia}}
DiccionarioEstudiantes = {"Colegio1": {"Cantidad": colegio1.Cantidad}, "Colegio2": {"Cantidad": colegio2.Cantidad}}
DiccionarioColegio1 = {**DiccionarioProfesores["Colegio1"], **DiccionarioEstudiantes["Colegio1"]}
DiccionarioColegio2 = {**DiccionarioProfesores["Colegio2"], **DiccionarioEstudiantes["Colegio2"]}
DiccionarioColegios = {**DiccionarioColegio1, **DiccionarioColegio2}
print(colegio1)
print(colegio2)
print(DiccionarioColegios)
print(repr(colegio1))
print(f"{colegio1:Horario}")
print(repr(colegio2))
print(f"{colegio2:Horario}")
print(DiccionarioProfesores)
print(DiccionarioEstudiantes)
print(DiccionarioColegio1)
print(DiccionarioColegio2)

