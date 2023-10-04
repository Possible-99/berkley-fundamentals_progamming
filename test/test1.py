
# 
def make_withdraw(balance):
    def withdraw(amount):
        #nonlocal balance                 # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        # balance = balance - amount       # Re-bind the existing balance name
        return balance
    return withdraw
    
def hello(name):
    def hi(x) : 
        if name != 11: print(name + x)
        return name
    
    return hi

    
def test(x):
    def test2():
        # x = x + 2
        print(x)

    return test2
    
    
# w = make_withdraw(100)
# w(30)

# a = hello(12)
# a(13)    

# test(2)()
print(make_withdraw(2)(1))