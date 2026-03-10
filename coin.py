n, s = map(int, input().split())
slxu=0
if s % n != 0:
  slxu= (s // n) + 1
else:
  slxu = s// n
print(slxu)