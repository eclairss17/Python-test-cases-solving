// count the no of words in a sentence, cat and dog if the occurences are same return True else False

def cat_dog_count(arg):
  substring1 = "cat"
  substring2 = "dog"
  count1 = arg.count(substring1)
  count2 = arg.count(substring2)
  if count1 == count2 :
    return True
  else :
    return False 