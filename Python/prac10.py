# Write a python program to create a multiple inheritance using two super classes as Ferrari, Benz and the subclass as Car

class Ferrari:
    def __init__(self, model):
        self.model = model

class Benz:
    def __init__(self, model):
        self.model = model

class Car(Ferrari, Benz):
    def __init__(self, model, color):
        self.color = color

        Ferrari.__init__(self, model)
        Benz.__init__(self, model)

        print(self.model)
        print(self.color)

my_car = Car(model="Benz", color="Orange")
my_car = Car(model="Ferrari", color="Black")


#output: 

#Benz
#Orange
#Ferrari
#Black
