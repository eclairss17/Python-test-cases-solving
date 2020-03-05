#Return True if a palindrome

def is_palindrome(s):
  left_Pos=0
  right_Pos=len(s)-1
  while right_Pos>=left_Pos:
    if not s[left_Pos]==s[right_Pos]:
      return False
    left_Pos+=1
    right_Pos-=1
    return True