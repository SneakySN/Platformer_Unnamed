from collections import namedtuple

Position  = namedtuple("Position" , "x y")
Scale     = namedtuple("Scale"    , "scale")
Image     = namedtuple("Image"    , "source")
Sprite    = namedtuple("Sprite"   , "sprite")
Cursor    = namedtuple("Cursor"   , "")
Clickable = namedtuple("Clickable", "")
Clicked   = namedtuple("Clicked"  , "")
