c=input()
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"

if c in upper:
    i = upper.index(c)
    n= lower[i]
elif c in lower:
    i=lower.index(c)
    n= upper[i]
else:
    n=c
print(n)
    