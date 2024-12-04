class Shipping:

    def calculate_weight(self,weight):

        print(weight*5)

class Express_shipping(Shipping):

    def calculate_weight(self,weight):

        print(weight*20)

class Standard_shipping(Express_shipping):

    def calculate_weight(self,weight):
        
        print(weight*10)

standard_instance=Standard_shipping()

exp=Express_shipping()

ship=Shipping()

standard_instance.calculate_weight(10)

exp.calculate_weight(10)

ship.calculate_weight(10)

ship.calculate_weight(10)

