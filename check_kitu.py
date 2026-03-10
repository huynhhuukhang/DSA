c=input()
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
digit="0123456789"
if c in upper:
    print("UPPER")
elif c in lower:
    print("LOWER")
elif c in digit:
    print("DIGIT")
else:
    print("SPECIAL")
