from collections import namedtuple

# Generic components
Position  = namedtuple("Position" , "x y")
Scale     = namedtuple("Scale"    , "value")
ZIndex    = namedtuple("ZIndex"   , "value")
Image     = namedtuple("Image"    , "value")
Sprite    = namedtuple("Sprite"   , "value")
Cursor    = namedtuple("Cursor"   , "")
Clickable = namedtuple("Clickable", "")
Clicked   = namedtuple("Clicked"  , "")

# Menu components
MenuButton = namedtuple("MenuButton", "id")
