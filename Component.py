from collections import namedtuple

Position  = namedtuple("Position" , "x y")
Scale     = namedtuple("Scale"    , "value")
ZIndex    = namedtuple("ZIndex"   , "value")
Image     = namedtuple("Image"    , "value")
Sprite    = namedtuple("Sprite"   , "value")
Cursor    = namedtuple("Cursor"   , "")
Clickable = namedtuple("Clickable", "")
Clicked   = namedtuple("Clicked"  , "")
