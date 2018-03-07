#Daniel
#2/9/18
#yield.py prints a yield sign

from ggame import*

white = Color(0xFFFFFF,1)
red = Color(0xFF0000, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(1, black)
redOutline = LineStyle(1, red)
whiteOutline = LineStyle(1, white)

triangle1 = PolygonAsset([(0,0), (200,0), (100,173.205)], blackOutline, white)
triangle2 = PolygonAsset([(5,0), (195,0), (100, 164.205)], redOutline, red)
triangle3 = PolygonAsset([(50,50), (150,50), (100,129.205)], whiteOutline, white)
text = TextAsset("YIELD", fill = red, style = "bold 10pt Arial")

Sprite(triangle1, (0,1))
Sprite(triangle2, (5,4))
Sprite(triangle3, (50,50))
Sprite(text, (80,75))

App().run()
