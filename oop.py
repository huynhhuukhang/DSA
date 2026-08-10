class Animal:
    def __init__(self,name,mass):
        self.name=name
        self.mass=mass
    
    def __del__(self):
        print(f"{self.name} da duoc huy")


dog=Animal("Dog",30)
print(dog.name)
print(dog.mass)

del dog

