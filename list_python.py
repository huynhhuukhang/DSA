list1 = [1,2,3,4,5,6,7]

list3 = [9,10]
list1.append(8)
print(list1)

list2=list1.copy()
print(list2)


list1.extend(list3)
print(list1)

print(list1.index(7))

list1.append(8)
print(list1)
print(list1.count(8))

list1.insert(-1,11)
print(list1)

x=list1.pop()
print(x)
print(list1)

list1.remove(11)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)