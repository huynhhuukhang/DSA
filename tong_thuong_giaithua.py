n=int(input())
gt=1
tong=1.0
for i in range(1,n):
   gt*=i
   tong+= 1/gt
print("%.4f" % tong)