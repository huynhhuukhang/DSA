num=int(input())
def maximum69Number (num: int) -> int:
    nine=0
    six=0
    while num>0:
        a=num%10
        if a%6==0: six+=a
        else:nine+=a
        num//10
