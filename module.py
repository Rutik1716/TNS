import math
import random

def perimeter(l,b):
    return 2*(l+b) #Perimeter of rectangle

def area_circle(r):
    return math.pi * r *r #Area of circle

print("This is a module for calculating perimeter and area.")

if __name__ == "__main__":
    print("Perimeter:", perimeter(random,random))
    print("Area:", area_circle(random))