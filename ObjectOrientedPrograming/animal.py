
class Animal:

    name:str

    species:str

    def __init__(self,name,species):
        
        self.name=name

        self.species=species

    def __str__(self):

        return self.name
    

class Lion(Animal):

    def __init__(self,name,species):
        
        super().__init__(name,species)

    def sound(self):

        print("roar....")

lion_instance=Lion("lion","carnivorous")

lion_instance.sound()

print(lion_instance)


class Cat(Animal):

    def __init__(self, name, species):

        super().__init__(name, species)

    def sound(self):

        print("meowwwww")

cat_instance=Cat("cat","carnivours")

cat_instance.sound()

print(cat_instance)