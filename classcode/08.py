from datetime import date

today = date(2015,2,20)
freedom = date(2015,5,12)

print(str(freedom - today))
print(today.strftime('%A %B %d'))



s = 'Hello'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s)
a = 'A'
print(ord(a))
print(hex(ord(a)))




from unicodedata import name, lookup
print(name('A'))
print(name('a'))
print(lookup('WHITE SMILING FACE'))
print(lookup('SNOWMAN'))
print(lookup('BABY'))
print(lookup('BABY').encode())


def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(100)
print(withdraw(25))
print(withdraw(25))
print(withdraw(75))