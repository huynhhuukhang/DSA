a,b,k = map(int, input().split())
p=0
t=0
if k % 2 !=0:
  p= a*((k//2) +1)
  t=b*(k//2)
  print(p-t)
else:
  p= a*(k//2)
  t= b*(k//2)
  print(p-t)