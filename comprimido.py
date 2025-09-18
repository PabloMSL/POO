class producto:
    print("esta clase es nueva")
    def __format__ (self, formato):
        if formato ==  "precio":
            return f"El precio es {self.precio}"
        return str(self)    
    def __init__(self, precio, producto):
        self.precio = precio
        self.producto = producto
    def __str__ (self):
        return f"El producto es {self.producto} y su precio es {self.precio}"
    def __repr__ (self):
        return f"producto(precio = {self.precio}, producto = {self.producto})"
acetaminofen = producto(2000, "acetaminofen")
print(acetaminofen)
print(repr(acetaminofen))
print(f"{acetaminofen:precio}")               