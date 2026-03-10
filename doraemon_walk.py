n,m=map(int,input().split())
y=n
x=(n+1)//2
step=((x+m-1) // m)* m
if x <= step <= y and step%m==0:
    print(int(step))
else:
    print('-1')