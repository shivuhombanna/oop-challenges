class Account:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self._balance=0
    def check_balance(self):
        print(f"balance : {self._balance}")
    def deposit_balance(self,amount):
        self._balance+=amount
        print(f"Success fully updated Balence{self._balance}")
    def withdra_amount(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"Sucess fully withdrwa {self._balance}")
        else:
            print("Low balance ")



class Savingsacc(Account):
    def calculate_intrest(self):
        INTREST_RATE=0.04 #4%
        intrst=self._balance * INTREST_RATE
        print(f"Intrsted amount is : {intrst}")


class Curentacc(Account):
    def withdra_amount(self, amount):
        over_lodeddamount=1000
        if self._balance + over_lodeddamount >=amount:
            self._balance-=amount
        else:
            print("amount is over lodedd")

class Bank:
    def __init__(self,id,city):
        self.id=id
        self.city=city
        self.__account={}
    def create_account(self,id,name,type):
        if type=="saving":
            new_account=Savingsacc(id,name)
        elif type=="curent":
            new_account=Curentacc(id,name)
        self.__account[id]=new_account
        return new_account
    def get_account(self):
        if id not in self.__account:
            print("account is not found")
        else:
            account=self.__account[id]
            print(f"id is :{account.id} \n older name is: {account.name}")
            return account

hbm=Bank("bank of mydur","mydur")
s1=hbm.create_account("1","shivu","saving")
s1.deposit_balance(100)
s1.check_balance()
s1.withdra_amount(10)
s1.check_balance()
s1.calculate_intrest()
