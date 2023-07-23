import math
class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
    
    def calculate_area(self):
        area = 3.14 * self.diameter**2 / 4 
        return area
    
    def calculate_perimeter(self):
        perimeter = 3.14 * self.diameter
        return perimeter

dia1 = 10
circle1 = Circle(dia1)
print(f"The area is {circle1.calculate_area():.2f} m^2")
print(f"The perimeter is {circle1.calculate_perimeter():.2f} m")
