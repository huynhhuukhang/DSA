thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print("###########")
thistuple1 = ("apple", "banana", "cherry")
for i in range(len(thistuple1)):
  print(thistuple1[i])


print("###########")
thistuple2 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple2):
  print(thistuple2[i])
  i = i + 1
print("###########")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print("###########")
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
print("###########")
t1 = ("a", "b", "a", "c")

print(t1.index("a"))

t = ("a", "b", "a", "c")

print(t.index("a", 1))


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)