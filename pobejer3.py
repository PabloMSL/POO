class Empresa:
    def __init__ (self, Nombre, Presupuesto, Ciudad, Empleados):
        self.Nombre = Nombre
        self.Presupuesto = Presupuesto
        self.Ciudad = Ciudad
        self.Empleados = Empleados
empresa1 = Empresa("Google", 1000000, "California", 5000)
print(empresa1.Nombre, empresa1.Presupuesto, empresa1.Ciudad, empresa1.Empleados)