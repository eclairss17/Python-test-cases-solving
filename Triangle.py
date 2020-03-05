#Class Triangle
from math import sqrt
class Point : 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        return sqrt((self.x-other.x)**2+ (self.y-other.y)**2)
        
class Triangle(Point) : 
    def __init__(self,p1,p2,p3) :
        #Point.__init__(self,p1,p2,p3)
        self.a = p1.distance(p2)
        self.b = p2.distance(p3)
        self.c = p3.distance(p1)
    def perimeter(self):
        return self.a+self.b+self.c
    def area(self):
        s = (self.a + self.b + self.c)/2  
        return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

p1 = Point(0,0)
p2 = Point(3,3)
p3 = Point(3,0)

#p1.distance(p2)

t = Triangle(p1,p2,p3)
print(t.perimeter())
print(t.area())