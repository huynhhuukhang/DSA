def minimumDistance(word: str) -> int:
    n = len(word)
    # Chúng ta dùng 1D DP để tối ưu. 
    # dp[j] là chi phí nhỏ nhất khi một ngón tay ở phím word[i-1] 
    # và ngón tay còn lại ở phím j.
    # j = 26 sẽ đại diện cho trạng thái "chưa đặt ngón tay xuống".
    
    dp = [0] * 27 
    BIG = 2**30
    dp = [0] * 27 # phím 0-25, và phím 26 là "trạng thái trống"

    def getDist(p, q):
        if p == 26: return 0 # Nếu ngón tay đang ở trạng thái trống, phí = 0
        return abs(p // 6 - q // 6) + abs(p % 6 - q % 6)

    # Khởi tạo: Ngón 1 đã ở word[0], ngón 2 đang ở trạng thái 26 (trống)
    # Vì vậy ban đầu mọi dp[j] là vô cùng, trừ dp[26] = 0
    dp = [BIG] * 27
    dp[26] = 0 

    for i in range(1, n):
        cur = ord(word[i]) - 65
        prev = ord(word[i-1]) - 65
        new_dp = [BIG] * 27
        
        for j in range(27):
            if dp[j] == BIG: continue
            
            # Lựa chọn 1: Dùng ngón tay vừa gõ (ở prev) gõ tiếp cur
            new_dp[j] = min(new_dp[j], dp[j] + getDist(prev, cur))
            
            # Lựa chọn 2: Dùng ngón tay còn lại (đang ở j) gõ cur
            # Sau đó ngón tay "kia" sẽ ở vị trí prev
            new_dp[prev] = min(new_dp[prev], dp[j] + getDist(j, cur))
            
        dp = new_dp

    return min(dp)

word = input().upper()
print(minimumDistance(word))