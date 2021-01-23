class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        output = ""
        for shape_height in range(0, self.height):
            for shape_width in range(0, self.width):
                output += "*"
            output += "\n"
        return output

    def get_amount_inside(self, shape):
        heights_inside = self.height // shape.height
        widths_inside = self.width // shape.width
        return heights_inside * widths_inside

    def __str__(self):
        output = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return output

class Square(Rectangle):

    def __init__(self,side):
        self.height = side
        self.width = side

    def set_width(self,width):
        self.width = width
        self.height = width

    def set_height(self,height):
        self.height = height
        self.width = height

    def set_side(self,side):
        self.height = side
        self.width = side

    def __str__(self):
        output = "Square(side=" + str(self.width) + ")"
        return output