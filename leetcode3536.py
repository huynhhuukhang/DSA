
n=int(input())
s=str(n)
num=[]
for c in s:
    num.append(int(c))

num.sort()
print(num[-1]*num[-2])

