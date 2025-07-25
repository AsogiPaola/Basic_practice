
class Producto:

    def __init__(self, id, describe, cost):
        self.id = id
        self.describe = describe
        self.cost = cost

    def create_label(self):
        return " %s \n %s \n %0.2f \n" %(self.id,
                                        self.describe,
                                        self.cost)
    
#clases hijas
class Perecedero(Producto):
    def __init__(self, id, describe, cost, caduce_date):
        super().__init__(id, describe, cost) #apuntador a la clase madre  
        self.caduce_date = caduce_date 

    def create_label(self):
        return super().create_label() + " %s \n" % self.caduce_date
    
class Electronico(Producto):
    def __init__(self, id, describe, cost, brand):
        super().__init__(id, describe, cost)
        self.brand = brand

pro = Producto("g", "Generico", 100.10)
per = Perecedero("p", "tomate", 200, "20-12-2026")
elec = Electronico("e", "Licuadora", 1000, "Ninja")

""" print(pro.create_label())
print(per.create_label())
print(elec.create_label()) """

#polimorfismo
objects = (pro, per, elec)

for object in objects:
    print(object.create_label(), type(object))

