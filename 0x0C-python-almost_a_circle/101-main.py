#!/usr/bin/python3

from models.square import Square
from models.rectangle import Rectangle

square = Square(250, 2,2)
print(square)
square.draw([Rectangle(76, 89), Rectangle(105, 140)],[square, Square(55), Square(42)])
