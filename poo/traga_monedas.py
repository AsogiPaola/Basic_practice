#obtener un numero aleatorio
from random import randint 

class TragaMonedas:
    #constructor usando metodo init de inicializacion
    def __init__(self, id, premio):
        self.id = id
        self.premio = premio
        #no esta dentro del constructor, no es obligatorio
        self.monedas = 0 

        #nadie ha ganado el premio mayor aun
        self.jackpots = 0  

    #para que al llamar el objeto n o me imprima el lugar en memoria de este mismo
    def __str__(self):
        return "Id:" + str(self.id) + " - Premio: " + str(self.premio)

    def __eq__(self, other):  #equal than
        return self.monedas == other.monedas

    def __lt__(self, other): #less than
        return self.monedas < other.monedas 
    
    def __gt__(self, other): #great than
        return self.monedas > other.monedas 
    
    def jugar(self):
        self.monedas += 1
        #tres numeros aleatorios de 0 a 9
        numeros = randint(0, 9), randint(0, 9), randint(0, 9)
        mensaje = ""
        if numeros[0] == [1] == [3]:
            self.jackpots += 1
            mensaje ="JACKPOT, Felicidades GANASTE!! %0.2f" % self.premio
        else:
            mensaje = "Mejor Suerte para la proxima!"
        return numeros, mensaje

tragamonedas_a =  TragaMonedas(1, 1000.00)
tragamonedas_b =  TragaMonedas(2, 700.00)

for i in range(200):
    print(tragamonedas_a.jugar())
    print(tragamonedas_b.jugar())

""" print("Monedas de tragamonedas a", tragamonedas_a.monedas)
print("Monedas de tragamonedas b",tragamonedas_b.monedas)   
print("Jackpot de tragamonedas a", tragamonedas_a.jackpots)
print("Jackpot de tragamonedas b",tragamonedas_b.jackpots)  """

print(tragamonedas_a == tragamonedas_b)
print(tragamonedas_a.__eq__(tragamonedas_b))
print(tragamonedas_a.__str__())

