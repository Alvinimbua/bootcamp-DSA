#!usr/bin/python

#solution to the compare triplets question

def compareTriplets(a,b):
    ans = []
    c = 0
    d = 0

    for i in range(0,len(a)):
        if a[i]>b[i]:
            c=c+1
        elif b[i]>a[i]:
            d=d+1
        else: 
            continue
        ans.append(c)
        ans.append(d)
        return ans

