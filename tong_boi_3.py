n=int(input())
sum=0
#1 + 1/2 + 1/3 + ... + 1/n
for i in range(1,n+1):
    sum += (i**3)
print(sum)