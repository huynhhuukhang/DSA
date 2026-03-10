a,b,c,n= map(int,input().split())
t=(a+b+c+n)
if t % 3 == 0:
    res= t//3
    if res>= a and res >=b and res >=c:
        print("YES")
    else:
        print("NO")
else:
    print("NO")