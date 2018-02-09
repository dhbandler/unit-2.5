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
triangle2 = PolygonAsset([(5,5), (195,5), (100, 168.205)], redOutline, red)
triangle3 = PolygonAsset([(50,50), (100,123.205), (150,50)], whiteOutline, white)

Sprite(triangle1)
Sprite(triangle2)
Sprite(triangle3)

App().run()
