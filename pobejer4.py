class Granja:
    def __init__ (self, Nombreanimal, Benefecios, Cantidad, Tipoanimal, Parcela):
        self.Nombreanimal = Nombreanimal
        self.Benefecios = Benefecios
        self.Cantidad = Cantidad
        self.Tipoanimal = Tipoanimal
        self.Parcela = Parcela
granja1 = Granja("Vacas", "Leche", 20, "Bovino", "Parcela 5")
print(granja1.Nombreanimal, granja1.Benefecios, granja1.Cantidad, granja1.Tipoanimal, granja1.Parcela)