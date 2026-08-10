sochai=int(input())

change=int(input())

res=sochai
while sochai >= change:
    ans=(sochai // change)
    res+=ans
    du=sochai%change
    sochai=du+ans

print(res)

