def fun():
    print("qua la vui")
fun()

def evenOdd(x):
    if(x%2==0):
        return "even"
    else:
        return "odd"
print(evenOdd(20))
print(evenOdd(17))
#1. Default Arguments
def myFun(x,y=50):
    print("x: ", x)
    print("y: ", y)
myFun(100)
#2. Keyword Arguments
def sinhvien(ho,ten):
    print(ho,ten)
sinhvien(ho="huynh", ten="huu khang")
#3.Positional Arguments
def thongtin(diachi, tuoi):
    print('i live in: ',diachi)
    print('toi: ',tuoi)

thongtin('tp can tho', 20)
thongtin(20,'tp can tho')

#4. Arbitrary Arguments
def myTest(*args, **kwargs):
    print("Non-keyword arguments (*args):")
    for arg in args:
        print(arg)
    print("\nKeyword arguments (**kwargs):")
    for key,value in kwargs.items():
        print(f"{key}=={value}")

myTest('hey','welcome', first='A', mid='B',last='C')


def func1():
    s='toi yeu em'
    def func2():
        print(s)
    func2()
func1()

#ham de quy
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))