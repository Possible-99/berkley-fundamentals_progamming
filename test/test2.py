class Account:
    interest = 0.02            # A class attribute
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    # Additional methods would be defined here




a  = Account("Juan")
b  = Account("jfdka")
Account.interest = 22

print(a.interest)