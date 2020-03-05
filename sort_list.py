#sorting a list of tuples, having first element string and second element is the no of occurences of that element
# sort from highest to lowest
def sort_list(data_list):
  return sorted(data_list,key=lambda x:(-x[1],x[0]))
