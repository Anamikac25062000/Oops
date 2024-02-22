# 3)Write a Python class, Square, and define two methods that return the square area and perimeter.


class Square:
    def __init__(self, square_side):
        self.square_side = square_side

    def square_area(self):
        return self.square_side * self.square_side

    def square_perimeter(self):
        return 4 * self.square_side

second_square = Square(8)

area = second_square.square_area()
perimeter = second_square.square_perimeter()

print("Square Area:", area)
print("Square Perimeter:", perimeter)
