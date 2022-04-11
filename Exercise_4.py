def triangle_type(a: int, b: int, c: int):
    triangle_sides = {a, b, c}  # set choose only unique values
    unique_sides = len(triangle_sides)
    if unique_sides == 3:
        return "scalene triangle"
    elif unique_sides == 2:
        return "isosceles triangle"
    elif unique_sides == 1:
        return "equilateral triangle"


print(triangle_type(2, 2, 3))