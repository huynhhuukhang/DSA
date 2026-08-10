n=int(input())


def isThree(n: int) -> bool:
    cnt=0
    k=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
        else:
            k+=1

    if cnt==3 and k!=0: return True
    else: return False


print(isThree(n))