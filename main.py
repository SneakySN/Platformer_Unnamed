import arcade
from Consts import *
from MenuView import *

def main():
	window = arcade.Window(SCREEN_W, SCREEN_H, "Platformer")
	window.show_view(MenuView())
	arcade.run();

if __name__ == "__main__":
	main()
