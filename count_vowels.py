#count the no of vowels in a string
def count_vowels(s):

    string=s.lower()
    characters=[]
    count=0
    vowels=['a','e','i','o','u']
    for i in range (0,len(string)):
        if string[i] in vowels:
            count+=1
    return count
