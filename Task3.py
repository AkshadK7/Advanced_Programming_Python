'''

Q] A class constructed by a radius and two methods which will compute the area and the perimeter of a circle.

'''


# Program :

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(6)
print(NewCircle.area())
print(NewCircle.perimeter())
