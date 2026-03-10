a1,a2,a3,b1,b2,b3= map(int,input().split())
n=int(input())
tong_so_hc=b1+b2+b3
tong_so_cup=a1+a2+a3
so_ke_hc=0
so_ke_cup=0
if tong_so_cup % 5 ==0:
    so_ke_cup=tong_so_cup//5
else:
    so_ke_cup=tong_so_cup//5 +1
if tong_so_hc % 10 ==0:
    so_ke_hc=tong_so_hc//10
else:
    so_ke_hc=tong_so_hc//10 +1
if(so_ke_cup + so_ke_hc <=n):
    print("YES")
else:
    print("NO")