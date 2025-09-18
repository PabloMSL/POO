class Restaurante:
    def __format__ (self, formato):
        if formato ==  "Menu":
            return f"El Menu de hoy es {self.Menu}"
        return str(self)    
    def __init__(self, Menu, Mesa, Mesero, Precio, Cantidad):
        self.Menu = Menu
        self.Mesa = Mesa
        self.Mesero = Mesero
        self.Precio = Precio
        self.Cantidad = Cantidad
    def __str__ (self):
        if self.Cantidad >0:
            if self.Cantidad == 1:
                return f"Seria {self.Cantidad} plato de {self.Menu} en la mesa {self.Mesa} atendido por {self.Mesero} y cuesta {self.Precio}"
            else:
                return f"Serian {self.Cantidad} platos de {self.Menu} en la mesa {self.Mesa} atendidos por {self.Mesero} y cuestan {self.Precio}"
        else:
            return "No hay platos disponibles"
    def __repr__ (self):
        return f"Comida = {self.Menu}, Precio = {self.Precio}"
print("Ingresa los datos del plato")
menu = input("Menu: ")
mesa = input("Mesa: ")
mesero = input("Mesero: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad de platos: "))
plato1 = Restaurante(menu, mesa, mesero, precio, cantidad)
print("Ingresa los datos de otro plato")
menu = input("Menu: ")
mesa = input("Mesa: ")
mesero = input("Mesero: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad de platos: "))
plato2 = Restaurante(menu, mesa, mesero, precio, cantidad)
print("Ingresa un tercer plato")
menu = input("Menu: ")
mesa = input("Mesa: ")
mesero = input("Mesero: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad de platos: "))
plato3 = Restaurante(menu, mesa, mesero, precio, cantidad)
DiccionarioplatosA = {"Plato1": {"Menu": plato1.Menu, "Mesa": plato1.Mesa, "Mesero": plato1.Mesero, "Precio": plato1.Precio, "Cantidad": plato1.Cantidad}, "Plato2": {"Menu": plato2.Menu, "Mesa": plato2.Mesa, "Mesero": plato2.Mesero, "Precio": plato2.Precio, "Cantidad": plato2.Cantidad}}
DiccionarioplatosB = {"Plato3": {"Menu": plato3.Menu, "Mesa": plato3.Mesa, "Mesero": plato3.Mesero, "Precio": plato3.Precio, "Cantidad": plato3.Cantidad}}
DiccionarioplatosC = {**DiccionarioplatosA, **DiccionarioplatosB}
print(plato1)
print(plato2)
print(plato3)
print(DiccionarioplatosC)
print(repr(plato1))
print(f"{plato1:Menu}")
print(repr(plato2))
print(f"{plato2:Menu}")
print(repr(plato3))
print(f"{plato3:Menu}")
print(DiccionarioplatosA)
print(DiccionarioplatosB)