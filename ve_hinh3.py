n=int(input())
num=1
for i in range(n):
    for j in range(n):
          print(num,end=" ")
          num+=1
    print()
print()
for i in range(1,n+1):
    for j in range(0,n):
          print(i+j,end=" ")
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n-i:
              print("~", end=' ')
        else:
             print(i, end=' ')
    print()
print()
for i in range(1,n+1):
    ktao=i
    kc=n-1
    for j in range(i):
        print(ktao, end=' ')
        ktao+=kc
        kc-=1
    print()
    