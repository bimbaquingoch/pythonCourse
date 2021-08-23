# clases
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


p1 = Point(1, 2)
p1.x = 11
print(p1.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Watashi wa {self.name}")


jotaro = Person("Kujo Jotaro")
jotaro.talk()

giorno = Person("Giorno Giovanna")
giorno.talk()
