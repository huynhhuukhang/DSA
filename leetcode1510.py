n=int(input())
def winnerSquareGame(n:int)->bool:
        dp= [False]*(n+1)
        for i in range(1,n+1):
            k=1
            while k*k<=i:
                if not dp[i-k*k]:
                    dp[i]=True
                    break
                k+=1
        return dp[n]

print(winnerSquareGame(n))