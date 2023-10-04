import functools
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    >>> m = Mint()
    >>> n = m.create(Nickel)
    >>> n.worth()
    5
    >>> n.year = 2015
    >>> n.worth()
    115
    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        return kind(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Mint.current_year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "The worth is a coin's face value + 1 cent for each year over age 50."
        "*** YOUR CODE HERE ***"
        # age = Mint.current_year - self.year
        # if age > 50:
        #     return self.cents + 50 - age
        # return self.cents
        return self.cents + max(0, Mint.current_year - self.year - 50)
        

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

    
    
#QuidditchPlayer

class QuidditchPlayer:
    def __init__(self, name, base_energy):
        """
        QuidditchPlayers have a name, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy

    def energy(self):
        return self.base_energy
    

class Beater(QuidditchPlayer):
    role = "bludgers"

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. 
        After playing for time minutes, Beaters lose their base energy level 
        divided by the number of minutes. If time is 0, catch the ZeroDivisionError 
        and print "You can't divide by zero!" instead.
        >>> fred = Beater("Fred Weasley", 640)
        >>> fred.energy(40)
        624.0
        >>> fred.energy(0)
        You can't divide by zero!
        """
        "*** YOUR CODE HERE ***"
        try:
            return self.base_energy - (self.base_energy / time)
        except ZeroDivisionError as e:
            print("You can't divide by zero!")
        
        
        
        
class Chaser(QuidditchPlayer):
    role = "score"
    energy_expended = 20

    def __init__(self, name, base_energy, goals):
        """
        Chasers have a name, score goals, and begin with base_energy.
        """
        "*** YOUR CODE HERE ***"
        super().__init__(name , base_energy)
        self.goals = goals
    
    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. For every goal 
        they score, they use energy_expended units of energy. In addition, they also use 
        10% of energy_expended if the number of minutes they have played is a multiple of 9.
        >>> katie = Chaser("Katie Bell", 230, 2)
        >>> katie.energy(20)
        190
        >>> ginny = Chaser("Ginny Weasley", 400, 3)
        >>> ginny.energy(45)
        338.0
        """
        "*** YOUR CODE HERE ***"
        used_energy = self.goals * self.energy_expended 
        used_energy += self.energy_expended* 0.1 if self.goals % 3 == 0 else 0

        return self.base_energy - used_energy

        
        
        
class Seeker(QuidditchPlayer):
    role = "snitch"
    energy_expended = 5

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. Seekers expend energy_expended 
        units of their energy for every minute they have been playing.
        >>> harry = Seeker("Harry Potter", 700)
        >>> harry.energy(30)
        550
        >>> harry.energy(20)
        600
        """
        "*** YOUR CODE HERE ***"
        return self.base_energy - time * self.energy_expended
        
        
        
class Keeper(QuidditchPlayer):
    role = "guard"
    energy_expended = 50

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. If less than 30 minutes have 
        passed, then Keepers do not lose any energy. If 30 minutes or more have passed, 
        then Keepers expend 80% of their energy_expended units for every full 15 
        minutes that pass.
        >>> oliver = Keeper("Oliver Wood", 380)
        >>> oliver.energy(45)
        260.0
        >>> oliver.energy(29)
        380
        """
        "*** YOUR CODE HERE ***"
        if time < 30 : return self.base_energy

        energy_used = (time / 15) * self.energy_expended * 0.8 
        return self.base_energy - energy_used 




def tax(shopping_cart, percent):
    """ Returns a new list where a `percent` tax is added to each item's price in a shopping cart.
    >>> fruit_cart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> tax(fruit_cart, 10)
    [('apple', 0.55, 3), ('banana', 0.275, 4)]
    >>> cal_cart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> tax(cal_cart, 100)
    [('oski', 2000.0, 1), ('go', 2.5, 2), ('bears', 7.0, 2)]
    """
    "*** YOUR CODE HERE ***"
    tax_multiplier= 1 + (percent / 100)
    return [(elem[0] , elem[1] * tax_multiplier, elem[2]) for elem in shopping_cart]



def total_cost(shopping_cart):
    """ Returns a float that is the total cost of all items in the shopping cart.
    >>> fruit_cart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> taxed_fruit = tax(fruit_cart, 10)
    >>> total_cost(taxed_fruit)
    2.75
    >>> cal_cart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> taxed_cart = tax(cal_cart, 100)
    >>> total_cost(taxed_cart)
    2019.0
    """
    "*** YOUR CODE HERE ***"
    return sum([elem[1] * elem[2] for elem in shopping_cart])