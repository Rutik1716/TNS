import module

len = int(input("Enter length of rectangle: "))
wid = int(input("Enter width of rectangle: "))
perimeter = module.perimeter(len, wid)
print("Perimeter:", perimeter)

rad = int(input("Enter radius of circle: "))
area = module.area_circle(rad)
print("Area:", area)