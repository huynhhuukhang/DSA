c=input()
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"

if c in upper:
    i = upper.index(c)
    if c=="Z":
       n="a"
    else:
       n= lower[i+1]
elif c in lower:
    i=lower.index(c)
    if c=="z":
        n="a"
    else:
        n= lower[i+1]
else:
    n="a"
print(n)
    