
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()
"""
print("Calculating rectangle areas:")
calculate_rectangle_area(9, 3)
calculate_rectangle_area(10, 5)
"""

# Triangle
def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area = 1/2 * height * base
    print(f"Triangle with Height {height} and Base {base}")
    print(f"Area = 1/2 × {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)