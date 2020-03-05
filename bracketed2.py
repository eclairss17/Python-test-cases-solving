#bracketed function alternative approach
def bracketed(s):
  list = s 
  for i in list : 
    if list[i] == '(' and list[i+1] == 's' and list[i+2] == ')':
      return True
    else :
      return False