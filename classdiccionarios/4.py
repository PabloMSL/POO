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