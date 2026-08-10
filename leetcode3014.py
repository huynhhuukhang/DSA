s=input()

def minimumPushes(s:str)->int:
    res=0
    for i in range(len(s)):
        res+=(i//8)+1

    return res

print(minimumPushes(s))