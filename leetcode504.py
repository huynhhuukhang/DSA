num=int(input())

def convertToBase7(num:int)->str:
    while num >0:
        a=num%7
        num//=7
        print(a)