#sort dictionary using key value pairs, roll no in this case

def sort_dict(student_data):
  return sorted(student_data, key = lambda i: i['rollno'])
