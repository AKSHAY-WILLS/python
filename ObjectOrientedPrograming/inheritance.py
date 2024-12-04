class GarandParent:

    def m(self):

        print("Grandparent class m method")

class Parent():

    def m(self):

        print("Parent class m method")

class Child(Parent,GarandParent):

    def m3(self):

        print("Child class m3 method")

Child_instance=Child()

Child_instance.m3()

Child_instance.m()