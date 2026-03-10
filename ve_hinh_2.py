n=int(input())
for i in range(1,n+1):
    print("*" * i)
print()
for i in range(n,0,-1):
    print("*" *i)
print()
for i in range(1,n+1):
    print(" "*(n-i) +"*"*i)
print()
for i in range(n,0,-1):
    print(" "*(n-i) +"*"*i)
print()
for i in range(1, n + 1):
    if i == 1:  # dòng đầu tiên
        print("*")
    elif i == 2:  # dòng thứ hai
        print("**")
    elif i == n:  # dòng cuối cùng
        print("*" * n)
    else:  # các dòng ở giữa
        print("*" + " " * (i - 2) + "*")