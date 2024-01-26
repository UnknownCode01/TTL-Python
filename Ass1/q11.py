print("Hello roll 21052410, input the sides of a triangle to print its area")

import math

def calculate_triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    
    area = calculate_triangle_area(side1, side2, side3)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The entered side lengths do not form a valid triangle.")
