class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'
    def deposit(self,amount):
        self.balance = self.balance + amount
        print('Deposit Accepted! ${} has just been added to your balance!'.format(amount))
    def withdraw(self,value):
        if value > self.balance:
            print('Not enough money in balance! Please withdrawn less')
        else:
            self.balance = self.balance - value
            print(f'Withdraw accepted! ${value} has just been withdrawn from your balance!')

acc = Account('Pedro',100)
print(acc)
acc.owner
acc.balance
acc.deposit(50)
acc.balance
acc.withdraw(75)
acc.balance
acc.withdraw(500)