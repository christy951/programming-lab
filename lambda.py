l=int(input("enter length:"))
b=int(input("enter breadth:"))
h=int(input("enter heigth:"))
x=lambda a:a*a
print("Area of square is",(x(1)))
y=lambda a,b: a*b
print("Area of rectangle is",(y(l,b)))
z=lambda a,b: 1/2*(a*b)
print("Area of triangle is",(z(b,h)))
