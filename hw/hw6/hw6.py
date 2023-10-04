"""
    Remember to use methods inside other methods, because maybe you are implementing again some behavior
    that is already a method, like in repeat where we use say and it also handle saving the lastMessage.
    
    
    Implement first the more specific methods and then the more general one's, the one's that use the other methods.
    
    Almost always the edge cases goes in the top of the method.

    
    How to solve deisgn problems:
    1. What are the characteristics of the things?
    2. What actions can someone perform
    
    Extra(code part):
    
    What actions are involved in others?
"""


class Person(object):
    """
    >>> steven = Person("Steven")
    >>> barb = Person("Barb")
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> barb.ask("listen to me repeat myself")
    'Would you please listen to me repeat myself'
    >>> barb.repeat()
    'Would you please listen to me repeat myself'
    >>> steven.repeat()
    'Hello, my name is Steven'
    """
    def __init__(self, name):
        self.name = name
        "*** YOUR CODE HERE ***"
        self.lastMessage = "I haven't say anithing"

    def say(self, stuff):
        "*** YOUR CODE HERE ***"
        self.lastMessage = stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        "*** YOUR CODE HERE ***"
        return self.say(self.lastMessage)

        
        
        
        
        


class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> sophia_account = Account('Sophia')
    >>> sophia_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> sophia_account.transactions
    [('deposit', 1000000)]
    >>> sophia_account.withdraw(100)      # buying dinner
    999900
    >>> sophia_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02
    balance = 1000

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Out of stock'
    >>> v.restock(2)
    'Stock: 2'
    >>> v.vend()
    'Please deposit $10 more'
    >>> v.deposit(7)
    'Current Balance: $7'
    >>> v.vend()
    'Please deposit $3 more'
    >>> v.deposit(5)
    'Current Balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change'
    >>> v.deposit(10)
    'Current Balance: $10'
    >>> v.vend()
    'Here is your candy'
    >>> v.deposit(15)
    'Out of stock. Here is your $15'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    "*** YOUR CODE HERE ***"

    def restock(self,  new_stock):
        self.stock += new_stock
        return "Stock: {}".format(new_stock)

    def deposit(self , money):
        if self.stock == 0 : return "Out of stock. Here is your ${}".format(money)
        self.balance += money
        return "Current Balance: ${}".format(self.balance)
    
    def vend(self):
        if self.stock == 0:
            return "Out of stock"
        change = self.balance - self.price
        if self.balance < self.price:
            return "Please deposit ${} more".format(-change)

        self.balance = 0
        self.stock -= 1

        return "Here is your candy" + (" and ${} change".format(change) if change > 0 else "")
        


class Arr88():
    """
    Arr88 is an object similar to Data 8 numpy arrays.
    Here the internel representation is a list
    """
    def __init__(self, values):
        # Check that all values are the same type, else it errors
        if len(values) > 1:
            assert all([type(values[0]) == type(values[i]) for i in range(len(values))]), "Arr88 must be of homogeneous type"
        self._values = values

    # DO NOT CHANGE THE __repr__
    # This displays the Arr88 nicely in the terminal
    def __repr__(self):
        return "Arr88(" + str(self._values) + ')'

    def __len__(self):
        """ Return the length of the Arr88

        >>> arr88 = Arr88([1, 2, 3])
        >>> len(arr88)
        3
        >>> arr88 = Arr88([1, 2, 3, 4])
        >>> len(arr88)
        4
        """
        "*** YOUR CODE HERE ***"
        return len(self._values)

    def item(self, i):
        """
        Get the item of the Arr88 at index i
        >>> arr88 = Arr88([1, 2, 3])
        >>> arr88.item(1)
        2
        >>> arr88.item(0)
        1
        """
        "*** YOUR CODE HERE ***"
        return self._values[i]
        

    def __add__(self, arr88):
        """ Add two Arr88s of the same length element by element

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a + arr88b
        Arr88([5, 7, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['He', 'Wor', '!'])
        >>> arr88b = Arr88(['llo', 'ld', ''])
        >>> arr88c = arr88a + arr88b
        >>> arr88c
        Arr88(['Hello', 'World', '!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88), "Arr88's of different len"
        "*** YOUR CODE HERE ***"
        return Arr88([self._values[idx] + arr88.item(idx) for idx in range(len(arr88))])


        

    def __mul__(self, arr88):
        """ Multiply two Arr88s of the same length componentwise

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4, 5, 6])
        >>> arr88a * arr88b
        Arr88([4, 10, 18])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88a = Arr88(['Na', 'Batman', '!'])
        >>> arr88b = Arr88([10, 1, 5])
        >>> arr88c = arr88a * arr88b
        >>> arr88c
        Arr88(['NaNaNaNaNaNaNaNaNaNa', 'Batman', '!!!!!'])
        """
        # Checks that the lengths are the same
        assert len(self) == len(arr88), "Arr88's of different len"
        "*** YOUR CODE HERE ***"
        return Arr88([self._values[idx] * arr88.item(idx) for idx in range(len(arr88))])
        
        

    def negate(self):
        """Negate an Arr88 with mutation

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88b = Arr88([4.0, -5.5, 0.0])
        >>> arr88a.negate()
        >>> arr88a
        Arr88([-1, -2, -3])
        >>> arr88b.negate()
        >>> arr88b
        Arr88([-4.0, 5.5, -0.0])
        """
        "*** YOUR CODE HERE ***"
        for idx in range(len(self._values)):
            self._values[idx] *= -1
        


    def apply(self, func):
        """ Apply a function to an Arr88

        >>> arr88a = Arr88([1, 2, 3])
        >>> arr88a.apply(lambda x : x * x)
        Arr88([1, 4, 9])
        >>> arr88a # We aren't mutating arr88a
        Arr88([1, 2, 3])
        >>> arr88b = Arr88([lambda x: x, lambda x: x + 1, lambda x: x + 2])
        >>> arr88c = arr88b.apply(lambda f: f(1))
        >>> arr88c
        Arr88([1, 2, 3])
        """
        "*** YOUR CODE HERE ***"
        # return Arr88(list(map(func , self._values)))
        return Arr88([func(elem) for elem in self._values])
        







