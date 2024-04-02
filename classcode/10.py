'''
Object Oriented Programming 
'''

class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

print(Clown.nose)
print(Clown.dance())


class Account:
    interest = 0.02 # A class attribute
    withdraw_fee = 0
    def __init__(self,account_holder) -> None:
      self.balance = 0
      self.holder = account_holder

    def deposit(self,amount):
        '''add amount to balance'''
        self.balance  = self.balance + amount
        return self.balance
    
    def withdraw(self,amount):
        '''subtract amount from balance if funds are avilable'''
        assert amount <= self.balance,'Insufficent funds'
        self.balance = self.balance - amount
        return self.balance

'''
Inheritance
'''
class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return super().withdraw(amount+self.withdraw_fee)
    

class Bank:
    '''
    A bank has accounts
    >>> bank = Bank()
    >>> john = bank.open_account('John',10)
    >>> jack = bank.open_account('Jack',5,CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    '''
    
    def __init__(self):
        self.accounts = []
    
    def open_account(self,holder,amount,kind=Account):
        account  = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)
    
    def too_big_to_fail(self):
        return len(self.accounts) > 1
    
class SavingAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return super().deposit(amount - self.deposit_fee)
    

'''
Linked List
'''
class Link:
    empty = ()
    def __init__(self,first,rest = empty) -> None:
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest
    #@property can turn the method into attribute,
    #you can use the name of method to call method with no ()
    @property
    def second(self):
        return self.rest.first
    @second.setter
    def second(self,value):
        self.rest.first = value


'''
Tree
'''
class Tree:
    def __init__(self,label,branches = []) -> None:
        self.label = label
        for branch in branches:
            assert isinstance(branch,Tree)
        self.branches = list(branches)
    
        
    


