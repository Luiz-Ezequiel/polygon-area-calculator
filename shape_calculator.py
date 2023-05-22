class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_height(self, new_heigth):
        self.height = new_heigth
    
    def set_width(self, new_width):
        self.width = new_width

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * self.height + 2 * self.width
    
    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        string = ''
        for _ in range(self.height):
            string += self.width * "*"+'\n'
        return string
    
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side
    