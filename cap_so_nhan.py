a,b,c,d=map(int,input().split())
if b%a==0:
    q=b/a
    if  c% (b*q)==0:
        if(d % (c*q)==0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")