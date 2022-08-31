class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = (self.width * "*") + "\n"
        picture *= self.height
        return picture

    def get_amount_inside(self, iArea):
        return self.get_area() // iArea.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.height = side
        self.width = side