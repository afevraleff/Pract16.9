class Figures:
    def __init__(self, type, x, y, width=0, height=0, rad=0):
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rad = rad
    def __str__(self):
        if self.type == "Rectangle":
            print(f"{self.type}({self.x}, {self.y}, {self.width}, {self.height})")
        elif self.type == "Circle":
            print(f"{self.type}({self.x}, {self.y}, {self.rad})")
        elif self.type == "Square":
            print(f"{self.type}({self.x}, {self.y}, {self.width})")

Rect1 = Figures("Rectangle", 1, 2, 10, 100)
Rect1.__str__()
Circ1 = Figures("Circle", 0, 1, 0, 0, 10)
Circ1.__str__()
Squ1 = Figures('Square', 1, 1, 10)
Squ1.__str__()

class Rectangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def param(self):
        print("Ширина:",  round((((self.x1-self.x0)**2 + (self.y1 - self.y0) ** 2) ** 0.5), 2),
              "Длина:",  round((((self.x2-self.x1)**2 + (self.y2 - self.y1) ** 2) ** 0.5), 2),
              "Площадь:", round((((self.x1-self.x0)**2 + (self.y1 - self.y0) ** 2) ** 0.5), 2) *
              round((((self.x2-self.x1)**2 + (self.y2 - self.y1) ** 2) ** 0.5), 2))

rect2 = Rectangle(0, 0, 2, 3, 4, 5)
rect2.param()

class Clients:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def bal(self):
        print(f'Клиент {self.name}. Баланс: {self.balance} руб.')

cl1 = Clients("Иван Петров", 50)
cl1.bal()

class Guests:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def output(self):
        print(f"{self.name}, {self.city}, статус \"{self.status}\"")


class Mentor(Guests):
    status = "Наставник"
    def __init__(self, name, city):
        self.name = name
        self.city = city

g1 = Mentor("Иван Петров", "г. Москва")
g1.output()
g2 = Guests("Филипп Киркоров", "г. Москва", "отчислен")
g2.output()