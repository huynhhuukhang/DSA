n=int(input())

sum1=0
sum2=0
cnt=0
for i in range(1,2*n+1):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
    
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

print(gcd(sum1,sum2))

def lcm(a,b):
    return a*b /(gcd(a,b))

print(lcm(sum1,sum2))