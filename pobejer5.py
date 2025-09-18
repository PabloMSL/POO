class SENA:
    def __init__ (self, Sede, Bloque, Salon, Programa):
        self.Sede = Sede
        self.Bloque = Bloque
        self.Salon = Salon
        self.Programa = Programa
Bloquec = SENA("SENA-CBA","Bloque C","Salon 202","Programacion de software")
print(Bloquec.Sede, Bloquec.Bloque, Bloquec.Salon, Bloquec.Programa)