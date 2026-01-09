############
class Balance():
    def __init__(self,balance=0):
        self.__balance = balance ## private

    @property
    def balance(self):
        return self.__balance
        
    def deposite(self,amount):
        if amount>0:
            self.__balance +=amount
        else:
            print("no")
    
    def withdraw(self,amount):
        if 0<amount <=self.__balance:
            self.__balance -=amount
        else:
            print("no")
    
b=Balance(5000)
print(b.balance)

b.deposite(2000)
print(b.balance)

b.withdraw(2000)
print(b.balance)