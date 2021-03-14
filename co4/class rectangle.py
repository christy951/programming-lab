class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def getArea(self):
         return self.l * self.b
		
    def getPerimeter(self):
        return 2*(self.l + self.b)
		
r1 = Rectangle(2,4)
r2=Rectangle(3,4)

print(r1.getArea())
print(r2.getArea())
if r1.getArea()>r2.getArea():
    print("Rectangle 1 is greater")
else:
    print("Rectangle 2 is greater")
if r1.getPerimeter()>r2.getPerimeter():
    print("Rectangle 1 has more perimeter")
else:
    print("Rectangle 2 has more perimeter")
