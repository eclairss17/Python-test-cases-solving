#return prime or square root of a perfect sqaure or none
import math
def primeorsquare(n) : 
    sr = math.sqrt(n) 
    if(((sr - math.floor(sr)) == 0)):
    # If square root is an integer 
        return  int(sr)
    # Corner cases 
    elif (n <= 1) : 
        return None
    if (n <= 3) : 
        return int(n)
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return None
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return None
        i = i + 6
  
    return int(n)
    

