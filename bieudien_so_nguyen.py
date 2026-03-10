N=int(input())
if N==1:
    print('-1')
else:
  if N%2==0:
    a=N//2
    print(a)
    for i in range(1,a+1):
        print(2,end=' ')
  else:
     a=(N-3)//2
     print(a+1)
     for i in range(1,a+1):
        print(2, end=' ')
     print("3")
   