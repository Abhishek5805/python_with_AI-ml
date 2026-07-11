class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def set_balance(self,new_balance):
        self.__balance=new_balance

    
account1=BankAccount("John",1000)
account1.set_balance(2000)
print(account1.name,account1._BankAccount__balance)