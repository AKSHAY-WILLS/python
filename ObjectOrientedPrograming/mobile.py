class Mobile:

    name:str
    price:int
    brand:str

    def __init__(self,name,price,brand):

        self.name=name
        self.price=price
        self.brand=brand
    
    def display(self):

        print(self.name,self.price,self.brand)

mobile_instance1=Mobile("Oppof19",15500,"Oppo")

mobile_instance1.display()


