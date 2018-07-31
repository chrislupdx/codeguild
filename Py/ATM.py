class ATM(object):
    def __init__(self, balance, interest, name):
        self.balance = 100000
        self.interest = 0.001
        self.name = 'name'
    def _str_(self):
        return "{}'s Bankaccount".format(self.name)
    def check_balance(self, amt):
        self.balance
        return 'Thank you {}. Your balance is now {}.'.format(self.name, self.balance)
    def deposit(self, amt):
        self.balance += amt
        return 'Thank you {}.'.format(self.name, self.balance)
    def check_withdrawl(self, amt):
        request = input('How much do you want to withdraw?')
        if int(request) > self.balance:
            print("BROKE")
    def withdrawl(self, amt):
        if self.balance - amt >= 0:
            self.balance -= amt
        return 'Thank you {}. Your balance is now {}.'.format(self.name, self.balance)
    def calc(self, amt):
        interest = (int(self.interest) * int(self.balance))
        print('Your interest is {}.'.format(interest))
p1 = ATM(100, .0001, 'P1')
print(p1.deposit(100))
print(p1.check_withdrawl(200))
