d1,d2,d3= map(int, input().split())
c1= d1+d2+d3
c2=2*(d1+d2)
c3=2*(d1+d3)
c4=2*(d2+d3)
print(min(c1,c2,c3,c4))