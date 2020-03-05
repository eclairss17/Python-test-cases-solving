#Class Linear Equations 
class LinearEquation:

    def __init__(self, a=1, b=1, c=0):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __str__(self):
        if self.b < 0:
            return '%sx - %sy = %s' % (self.a, -1*self.b, self.c)
        return'%sx + %sy = %s' % (self.a, self.b, self.c)
    
    def __add__(self, eq):
        """ Combine like terms by adding two linear equations together. """
        try:
            return LinearEquation(self.a + eq.a, self.b + eq.b, self.c + eq.c)
        except TypeError as e:
            print("Error!", e)
            return None
   
    def __repr__(self):
        if self.b < 0:
            return '%sx - %sy = %s' % (self.a, -1*self.b, self.c)
        return'%sx + %sy = %s' % (self.a, self.b, self.c)

    def isparallel(self, eq):
        if self.a*eq.b == self.b*eq.a and self.a*eq.c != self.c*eq.a:
            return True
        return False

    def intersects(self, eq):
        if self.a*eq.b != self.b*eq.a:
            return True
        return False

    def overlaps(self, eq):
        if self.a*eq.b == self.b*eq.a and self.a*eq.c == self.c*eq.a:
            return True
        return False

