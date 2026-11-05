import math
# Get radius from the user as a float
radius = float(input("Enter the radius as a float: "))
print()
# Calculate the diameter
diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}")
print()
# Calculate the circumference
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {circumference:.2f}")
print()
# Calculate the area
area = math.pi * radius**2
print(f"The area of the circle is {area:.3f}")
