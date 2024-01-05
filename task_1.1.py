# Create a class hierarchy for representing different types of geometric figures, such as rectangles, circles, and triangles.
# Each class should have attributes for defining the shape's characteristics, such as dimensions or parameters.
# Use inheritance and method overriding to define methods for calculating the area and perimeter of different shapes
# Possible shapes: Circle, Polygon, RegularPolygon(Polygon), Rectangle(RegularPolygon)


class Shape:
    ABSTRACT_AREA = 2

    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def get_area(self) -> int:
        raise NotImplementedError()

    def get_perimeter(self) -> int:
        raise NotImplementedError()


class Circle(Shape):
    PI = 3.14159265359

    def __init__(self, name: str, color: str, radius: int) -> None:
        super().__init__(name, color)
        self.radius = radius

    def get_area(self) -> int:
        return self.PI * self.radius**2

    def get_perimeter(self) -> int:
        return self.PI * self.radius * 2


class Polygon(Shape):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name, color)

    def get_area(self) -> int:
        raise NotImplementedError()

    def get_perimeter(self) -> int:
        raise NotImplementedError()


class RegularPolygon(Polygon):
    def __init__(
        self, name: str, color: str, num_of_sides: int, len_of_side: int, apothem: int
    ) -> None:
        super().__init__(name, color)
        self.num_of_sides = num_of_sides
        self.len_of_side = len_of_side
        self.apothem = apothem

    def get_area(self) -> float:
        return (self.num_of_sides * self.len_of_side * self.apothem) / 2

    def get_perimeter(self) -> int:
        return self.num_of_sides * self.len_of_side


class Rectangle(RegularPolygon):
    def __init__(
        self,
        name: str,
        color: str,
        num_of_sides: int,
        len_of_side: int,
        apothem: int,
        height: int,
        width: int,
    ) -> None:
        super().__init__(name, color, num_of_sides, len_of_side, apothem)
        self.height = height
        self.width = width

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return (self.width + self.height) * 2


polygon = RegularPolygon(
    name="Regular polygon", color="White", num_of_sides=8, len_of_side=10, apothem=6
)
rectangle = Rectangle(
    name="Rectangle",
    color="Red",
    num_of_sides=4,
    len_of_side=5,
    apothem=2.5,
    height=5,
    width=5,
)
circle = Circle(name="Circle", color="Blue", radius=6)


print(
    f"{circle.name} area is {round(circle.get_area(), 1)} and perimeter {round(circle.get_perimeter(), 1)}"
)
print(
    f"{polygon.name} area is {polygon.get_area()} and perimeter {polygon.get_perimeter()}"
)
print(
    f"{rectangle.name} area is {rectangle.get_area()} and perimeter {rectangle.get_perimeter()}"
)
