n=int(input())
for i in range(1,n+1):
    print("*" * i)
print()
for i in range(n,0,-1):
    print("*" *i)
print()
for i in range(1,n+1):
    print(" "*(n-i) +"*"*i)
print()
for i in range(n,0,-1):
    print(" "*(n-i) +"*"*i)
print()