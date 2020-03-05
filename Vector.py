#Class Vector and its operations
import math
class Vector:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return 'Vector(%s, %s, %s)' % (self.x, self.y, self.z)
    def __repr__(self):
        return 'Vector(%s, %s, %s)' % (self.x, self.y, self.z)

    def __rmul__(self,number):
        print (number)
        print('ss')
        mul = Vector()
        mul.x = self.x * number
        mul.y = self.y * number
        mul.z = self.z * number

        return mul

    def __add__(self, operand):
        return Vector(self.x + operand.x, self.y + operand.y, self.z + operand.z)

    def cross(self, operand):
        return Vector(self.y * operand.z - self.z * operand.y, self.z * operand.x - self.x * operand.z, self.x * operand.y - self.y * operand.x)


    def dot(self, operand):
        return (self.x * operand.x) + (self.y * operand.y) + (self.z * operand.z)

    def norm(self):
        return math.sqrt((self.x ** 2 + self.y ** 2 + self.z ** 2)) 
        