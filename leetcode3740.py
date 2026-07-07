from typing import List
nums=list(map(int,input().split()))
def minimumDistance(nums: List[int]) -> int:
    n=len(nums)
    ans=n+1
    for i in range(n-2):
        for j in range(i+1,n-1):
            if nums[i]!=nums[j]:
                continue
            for k in range(j+1,n):
                if nums[j]==nums[k]:
                    ans= min(ans,k-i)
                return ans
    return -1 if ans==n+1 else ans *2
        

print(minimumDistance(nums))