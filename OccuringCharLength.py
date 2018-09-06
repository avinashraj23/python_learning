a=input('INPUT STRING ')
b=sorted(set(a))
for x in range(0,len(b)):
    print(b[x],end="")
    print(a.count(b[x]),end=" ")