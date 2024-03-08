# Write a python class named Circle constructed by a radius and two methods which will compute the area and perimeter of a circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14159 * self.radius * self.radius
        return area

    def perimeter(self):
        perimeter = 2 * 3.14159 * self.radius
        return perimeter

radius_input = float(input("Enter radius: "))
my_circle = Circle(radius_input)

area_result = my_circle.area()
perimeter_result = my_circle.perimeter()

print(f"Area of the circle: {area_result}")
print(f"Perimeter of the circle: {perimeter_result}")


#output:

# Enter radius: 2
# Area of the circle: 12.56636
# Perimeter of the circle: 12.56636