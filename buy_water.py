n,a,b= map(int,input().split())
total=0
if a*1 < b*0.5:
    total=n//1* a
else:
    if n%2==0:
       total=n//2 * b
    else:
       total=n//2 * b + a
print(total)