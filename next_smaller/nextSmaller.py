#Returns the next small number, or -1 if smaller its itself or startswith 0
def next_smaller(x):
    x=str(x)   
    for i in range(2,len(x)+1):
        p=sorted(x[-i+1:])[::-1] #get last i+1 elements in descending order
        for j in range(len(p)):
            if p[j]<x[-i]: #if p at j(p[j]) is less than the pivot element (which is also the greatest in p )
                s=x[:-i]+p[j] #swap pivot and p[j] (not in place but in a new list)
                p.pop(j) #pop p[j]
                p.append(x[-i]) #append pivot element to p
                s+="".join(sorted(p)[::-1]) #sort p in descending order and add it  to the new list in which pivot was replaced
                if s[0]=="0":
                    return -1
                else:
                    return int(s)
                    
    return -1

print(next_smaller(2211))