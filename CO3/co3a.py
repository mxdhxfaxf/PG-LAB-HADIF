from threedgraphics import cuboid
from threedgraphics import sphere
from graphics import rectangle
from graphics import circle
l=int(input("Enter length of cuboid:"))
w=int(input("Enter width of cuboid:"))
h=int(input("Enter height of cuboid:"))
b=int(input("Enter breadth of cuboid:"))
print("Area of cuboid=",cuboid.area(l,w,h))
print("perimeter of cuboid=",cuboid.perimeter(l,b,h))
r=int(input("Enter the radius of sphere:"))
print("Area of sphere=",sphere.area(r))
print("perimeter of sphere=",sphere.perimeter(r))
l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
print("Area of rectangle=",rectangle.area(l,b))
print("Perimeter of rectangle=",rectangle.perimeter(l,b))
r=int(input("Enter radius of circle:"))
print("Area of Circle:",circle.area(r))
print("Perimeter of Circle:",circle.perimeter(r))
