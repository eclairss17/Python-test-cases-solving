#class for AP
class ArithmeticProgression():
    def __init__(self,A=1,D=1):
        self.a= A
        self.d= D
    def get(self,n):
        tn = self.a + (n - 1) * self.d
        return tn
    def sum(self,n):
        total= (n * (2 * self.a + (n - 1) * self.d)) / 2
        return total