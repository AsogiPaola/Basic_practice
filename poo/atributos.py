class Vehiculo:

    folio = 0
    COLORES = ("BLANCO", "AZUL", "ROJO")
    def __init__(self,color):
        Vehiculo.folio += 1
        self.serie = Vehiculo.folio
        self.set_color(color)

    def __str__(self):
        return str(self.serie) + " " + self.color
    
    def set_color(self, color):
        color = color.upper().strip()
        if color in Vehiculo.COLORES:
            self.color = color
        else:
            self.color = Vehiculo.COLORES[0]

vehiculo_a = Vehiculo("rojo")
vehiculo_b = Vehiculo("verde")

print(vehiculo_a, vehiculo_b)


























