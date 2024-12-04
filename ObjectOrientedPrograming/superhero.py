class Superhero:

    name:str

    suit:str

    def __init__(self,name,suit):

        self.name=name

        self.suit=suit
        
    def __str__(self):

        return self.name
    
class Spiderman:

    def __init__(self,name,suit):

        super().__init__(name,suit)

    