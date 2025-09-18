class helados:
    def __format__ (self, formato):
        if formato ==  "Sabor":
            return f"El Sabor es {self.Sabor}"
        return str(self)    
    def __init__(self, Cantidad, Numerodebolas, Sabor, Precio):
        self.Cantidad = Cantidad
        self.Numerodebolas = Numerodebolas
        self.Sabor = Sabor
        self.Precio = Precio
    def __str__ (self):
        if self.Cantidad >0:
            if self.Cantidad == 1:
                return f"Seria {self.Cantidad} helado es de {self.Sabor} y tiene {self.Numerodebolas} bolas y cuesta {self.Precio}"
            else:
                return f"Seria {self.Cantidad} helados son de {self.Sabor} y tienen {self.Numerodebolas} bolas y cuestan {self.Precio}"
        else:
            return "No hay helados disponibles"
        
    def __repr__ (self):
        return f"Sabor = {self.Sabor}, Precio = {self.Precio}"
print("Ingresa los datos del helado")
cantidad = int(input("Cantidad de helados: "))
numerodebolas = int(input("Numero de bolas: "))
sabor = input("Sabor: ")
precio = float(input("Precio: "))
helado1 = helados(cantidad, numerodebolas, sabor, precio)
print("Ingresa los datos de otro helado")
cantidad = int(input("Cantidad de helados: "))
numerodebolas = int(input("Numero de bolas: "))
sabor = input("Sabor: ")
precio = float(input("Precio: "))
helado2 = helados(cantidad, numerodebolas, sabor, precio)
Diccionariohelados = {"Helado1": {"Cantidad": helado1.Cantidad, "Numerodebolas": helado1.Numerodebolas, "Sabor": helado1.Sabor, "Precio": helado1.Precio}, "Helado2": {"Cantidad": helado2.Cantidad, "Numerodebolas": helado2.Numerodebolas, "Sabor": helado2.Sabor, "Precio": helado2.Precio}}
print(helado1)
print(helado2) 
print(Diccionariohelados)
print(repr(helado1))
print(f"{helado1:Sabor}")
print(repr(helado2))
print(f"{helado2:Sabor}")