#Decorators in python, returns None for negative arguement
def nonnegative(foo):
    def check(x):
        if x>=0:
            return foo(x)
        else:
            return None
    return check

@nonnegative
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*(fact(x-1))