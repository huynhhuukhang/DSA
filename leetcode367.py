n=int(input())

def isPerfectSquare(n:int)-> bool:
    i=1
    while i*i <=n:
        if i*i==n:
            return True
        i+=1
    return False
            
        
    
print(isPerfectSquare(n))