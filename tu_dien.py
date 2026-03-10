#How to Create a Dictionary
d1={"ho":'huynh', "ten_lot":'huu', "ten":'khang'}
print(d1)
d2=dict(a="huynh", b="huu", c="khang")
print(d2)
# Access using key
print(d1["ho"])
print(d1["ten_lot"])
print(d1["ten"])
# Access using get()
print(d1.get("ten"))
# Adding a new key-value pair
d1["tuoi"] = 20
print(d1)
del d1["tuoi"]
print(d1)
key, val=d1.popitem()
print(f"key: {key}, value: {val}")
d1.clear()
print(d1)
print("###################################")
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")