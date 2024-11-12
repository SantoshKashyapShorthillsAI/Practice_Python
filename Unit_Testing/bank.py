class InsufficientFunds(Exception):
    pass 

class bankaccount:
    def __init__(self, balance):
        self._balance =balance
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self , amount):
        if amount<=0:
            return ValueError
        
        self._balance+=amount

    def withdraw(self,amount):
        if amount>self._balance:
            return InsufficientFunds
        
        if amount<=0:
            return ValueError
        
        self._balance-=amount