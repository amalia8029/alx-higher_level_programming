#!/usr/bin/python3
"""defines Square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class for Square instances with
    attributes from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size
def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
@property
    def size(self):
        """gets private instance attribute size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets private instance attribute size and
        uses to set width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
 def update(self, *args, **kwargs):
        """assigns an argument to each attribute of Square"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        
         elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

 def to_dictionary(self):
        """returns dictionary representation of a Square"""
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["size"] = self.size
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        return dict_rep                     
