#tra ve chuoi doi xung nho nhat theo thu tu tu dien cua chuoi s
s=input()
def smallestPalindrome(s:str)->str:
    cnt=[0]*26
    for ch in s:
        cnt[ord(ch)-ord('a')]+=1
    left=[]
    mid=""
    for i in range(26):
        left.append( chr(i+ord('a')) * (cnt[i]//2))
        if cnt[i]%2==1:
            mid=chr(i+ord('a'))
    left="".join(left)
    return left+mid+left[::-1]

print(smallestPalindrome(s))