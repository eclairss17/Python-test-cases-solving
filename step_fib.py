#nested function that returns the skipped steps (k) for a fibonacci series n
def step_fib(k):
  a=[]
  g = 0
  def Fibonacci(n):
    if (n <= 0) : 
        return 0
    fibo =[0] * (n+1) 
    fibo[1] = 1
   
    # Initialize result 
    sm = fibo[0] + fibo[1] 
   
    # Add remaining terms 
    for i in range(2,n+1) : 
        fibo[i] = fibo[i-1] + fibo[i-2] 
        sm = sm + fibo[i] 
     
    c = len(fibo)-1
    #print(fibo)
    #print(c)
    i=0
    while i<c :
      if k > 0 :
      #for j in range(c):
        a.append(fibo[i])
        i = i + k
      elif k < 0 :
        a.append(fibo[i])
        i = i - k
    if k < 0 :
      list = a[::-1]
      #str = ''.join(str(e) for e in list)
      str1 = str(list).strip('[]')
      #str1 = map(lambda x: x.replace(' ', ''), str(list))
      str2 = "'"+str1+"'"
      str2 = str1.replace(" ","")
      return str(str2)
    else : 
      #str = ''.join(str(e) for e in a)
      str1 = str(a).strip('[]')
      str2 = "'"+str1+"'"
      str2 = str1.replace(" ","")
      return str(str2)
      #return a
  return Fibonacci

  
print(step_fib(-3))
  
print(step_fib(1))