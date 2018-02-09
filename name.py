#Daniel Bandler
#2/8/18
#name.py asks for name and hex code and prints them

from ggame import *

name = input("input your name here ")
code = input("input your Hexedecimal color code here ")
black = Color(0x000000, 1)

selectedColor = Color("0x"+code, .5)

selectedOutline = LineStyle(1,selectedColor)

text = TextAsset(name, fill = black, style = "bold 40pt Georgia")
background = RectangleAsset(1000, 1000, selectedOutline, selectedColor)

Sprite(text)
Sprite(background)

App().run()
