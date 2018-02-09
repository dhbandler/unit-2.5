#Daniel Bandler
#2/8/18
#name.py asks for name and hex code and prints them

from ggame import *

name = input("input your name here")
code = input("input your Hexedecimal color code here")

selectedColor = Color(code, 1)

text = TextAsset(name, fill = selectedColor, style = "bold 40pt Georgia")

Sprite(text)

App().run()
