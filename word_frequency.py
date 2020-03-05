#function to return word frequency of each word in a string case sensitive
def word_frequency(s,l):
    #s = s.casefold()
    split_it = s.split()
    it=s.split()
    
    wordfreq = []
    for w in split_it:
        wordfreq.append(split_it.count(w))
        #split_it.remove(w)
    x=list(zip(split_it, wordfreq))

    x=sorted(x, key = lambda z: z[1])
    
    size=len(x)
    i=1
    y=0
    p = []
    while l:
        y=x[size-i][1]
        for a in x:
            if a[1]==y:
                #print(wordfreq)
                i=i+1
                p.append(a)  
        l=l-1
    
    e =list(set([i for i in p]))
    e = sorted(e, key = lambda z:z[1], reverse = True)
    #print (e)
    return e
    
print(word_frequency('A aa A aa AAA aaa', 2))