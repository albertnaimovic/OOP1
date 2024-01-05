# Create two classes: Shape and Rectangle.
# The Shape class should have the following attributes: name and color.
# It should also have a method called get_area() that returns the abstract area of a shape.

# The Rectangle class should inherit from the Shape class
# and should have the following attributes: width and height.
# It should also override the get_area() method to calculate the area of a rectangle using its width and height.


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle", 4)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length: float) -> None:
        super().__init__(side_length, side_length)
        self.side_length = side_length


square = Square(5)
print(square.name)  # prints "Rectangle"
print(square.sides)  # prints 4
print(square.area())
