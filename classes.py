class Animal:
    def show():
        print("hello")
class Dog(Animal):
    def show():
        print("world")
class cat(Dog):
    pass

c1=cat()
print(c1.show)