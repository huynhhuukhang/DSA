from typing import List

nums=list(map(int,input().split()))
target=int(input())
start=int(input())


def getMinDistance(nums:List[int], target:int, start:int)->int:
    n=len(nums)
    for i ,num in enumerate(nums):
        if(num==target):
            n=min(n, abs(i-start))
    return n




print(getMinDistance(nums,target,start))