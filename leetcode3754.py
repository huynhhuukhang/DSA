# Concatenate Non-Zero Digits and Multiply by Sum I
n=int(input())
def sum(n:int)-> int:
    x=0
    sum=0
    for c in str(n):
        d= int(c)
        sum+=d
        if d >0:
            x=x*10+d
    
    return sum*x

print(sum(n))