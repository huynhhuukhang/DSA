from typing import List

a=list(map(int,input().split()))

def ham(a:List[int])->int:
    a.sort()
    n=len(a)
    sum=0
    

print(ham(a))