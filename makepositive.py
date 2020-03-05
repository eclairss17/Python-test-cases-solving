#Decorator to return positive if the function returns negative
def diff(a,b):
    return a-b
def makepositive(func):
    def plus(a,b):
        e=func(a,b)
        if(a<b):
            a,b=b,a
            c=func(a,b)
            return c
        return e
    return plus
d=makepositive(diff)
print(d(1,2))