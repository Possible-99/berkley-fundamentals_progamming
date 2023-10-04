class Vehicle:
    year= 2022
    
    def __init__(self , name , color):
        self.name =  name
        self.color=  color

    def move(self, x , y):
        print(x)
        print(y)


class Bycicle(Vehicle):
    def __init__(self, name, color):
        super().__init__(name, color)
    
    def run(self , l):
        print("Move")
        Vehicle.move(self, 1 , 2)

        
b1 = Bycicle("Bethon", "red")
b1.run(1)
print(b1.color)
print(b1.name)