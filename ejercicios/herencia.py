class Mammal:
    def walk(self):
        print("camina")


class Dog(Mammal):
    def corre(self):
        print("corre")


class Cat(Mammal):
    pass


dog = Dog()
cat = Cat()

dog.walk()
dog.corre()
cat.walk()
