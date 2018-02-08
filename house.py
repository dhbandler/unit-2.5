#Daniel Bandler
#2/8/18
#house.py design a house

from ggame import*

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
grey = Color(0xD3D3D3,1)
blue = Color(0x00FFFF, 1)
brown = Color(0xD2691E, 1)



blackOutline = LineStyle(1,black)

whiteRectangle = RectangleAsset(80, 60, blackOutline, white)
greyTriangle = PolygonAsset([(0,60), (100,60), (50,0)],blackOutline, grey)
blackRectangle = RectangleAsset(10 , 30, blackOutline, black)
blueRectangle = RectangleAsset(20, 20, blackOutline, blue)
brownRectangle = RectangleAsset(15,30, blackOutline, brown)


Sprite(greyTriangle)
Sprite(whiteRectangle, (10,60))
Sprite(blackRectangle, (75, 8))
Sprite(blueRectangle, (20, 75))
Sprite(blueRectangle, (60, 75))
Sprite(brownRectangle, (42.5, 90))


App().run()
