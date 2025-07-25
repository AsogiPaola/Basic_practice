

class Cuenta:

    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        #con  __ hacemos que no sea accesible de manera simple, es decir un dato privado
        self.__balance = 0.00
    
    def __str__(self):
        return "Name: " + str(self.name) + " Monto actual: " + str(self.__balance)

    def retirar(self, monto):
        if self.__balance >= monto:
            self.__balance -= monto
        else:
            print("No cuentas con suficiente dinero en tu cuenta para hacer este retiro, intenta nuevamente con un monto menor. ")

    def depositar(self, monto):
        if monto > 0:
            self.__balance += monto



cuenta = Cuenta("Paola", "Matias ramos")
cuenta.depositar(1000)
cuenta.retirar(200)
print(cuenta.__str__())
#print(cuenta._Cuenta__balance)