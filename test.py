s="huynh huu khang"
print(s)
a="""xin chao viet nam
la toi day
"""
print(a)
print(s[::-1])
s= s + " dep trai"
print(s)
print(len(s))
print(s.upper())
print(s.lower())
w="Python"
for char in w:
    print(char)
qq='    one piece    '
print(qq)
print(qq.strip())
#Formatting Strings
name='luffy'
age=19
print(f"Name: {name}, Age: {age}")
z="my name is {} and my age is {}".format("zoro", 22)
print(z)