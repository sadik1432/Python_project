
# Write a Python program to calculate area and perimeter of the circle.
from math import pi #import pi for mathemetical calculation

def PerimeterOfCircle(radius): #define function for calculating perimeter of the circle
    Perimeter= 2*pi*radius
    return Perimeter

def AreaOfCircle(radius): #define function for calculating area of the circle
    area= pi*radius**2
    return area
while (1):
    con = str(input("\nEnter Y for continue OR Any Key for exit: "))
    if con=="Y" or con=="y":
        x= float(input("\nEnter radius: ")) #input Radius
        print("Area of the circle with radius{} is: {:.2f}\n".format(x,AreaOfCircle(x)))
        print("The perimeter of the circle with radius {} is: {:.2f}".format(x,PerimeterOfCircle(x)))
    else:
        break