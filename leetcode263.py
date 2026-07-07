n=int(input())
def isUgly(n:int)->int:
    if n<2:
        return True
    for i in [2,3,5]:
        while n%i==0:
            n//=i
    return n==1     
print(isUgly(n))