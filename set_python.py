thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

myset = {"apple", "banana", "cherry"}
print(type(myset))

myset = ("apple", "banana", "cherry")
print(type(myset))

myset = ["apple", "banana", "cherry"]
print(type(myset))


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

print("##################################")
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))