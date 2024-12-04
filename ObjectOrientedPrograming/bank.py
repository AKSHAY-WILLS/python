#bank[acno,bal,ac_type,customer_name]

#initialize[deposite(amount)]

class Bank:

    acnt_number:int

    bal:int

    ac_type:str

    customer_name:str

    def __init__(self,acnt_number,bal,ac_type,customer_name):

        self.acnt_number=acnt_number

        self.bal=bal

        self.ac_type=ac_type

        self.customer_name=customer_name
    
    def deposite(self,amount):

        self.bal+=amount

        print(f"your account{self.acnt_number} has been credited with amount{amount} avl bal{self.bal}")

    def withdraw(self,amount):
        
        if self.bal<amount:
           
           print("insufficient balance")

        else:

            self.bal-=amount

            print(f"your account{self.acnt_number} has been debited with amount{amount} avl bal{self.bal}")


    def get_bal(self):
         
         print("your aval bal is",self.bal)

customer_instance1=Bank(128945,1000,"saving","Akshay")

customer_instance1.withdraw(500)

customer_instance1.get_bal()

customer_instance1.deposite(2)

customer_instance1.get_bal()

customer_instance1.withdraw(2000)

customer_instance1.get_bal()