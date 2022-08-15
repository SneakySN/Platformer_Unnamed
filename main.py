import arcade
from Consts import *
from MainView import MainView

def main():
	window = arcade.Window(SCREEN_W, SCREEN_H, "Platformer")
	window.show_view(MainView())
	arcade.run();

if __name__ == "__main__":
	main()
