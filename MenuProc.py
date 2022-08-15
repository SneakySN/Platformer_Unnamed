import arcade
from entitas import *
from Component import *
from Consts import *

class CreateMenuButtons(InitializeProcessor):
	def __init__(self, context: Context):
		super().__init__()
		self.context = context

	def initialize(self) -> None:
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 + 5 * 32, "assets/menu/start.png")
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 + 2 * 32, "assets/menu/setting.png")
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 - 1 * 32, "assets/menu/mapedit.png")
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 - 4 * 32, "assets/menu/quit.png")
		self.create_button(96, 32, "assets/menu/back.png")

	def create_button(self, x, y, img, extra_comp = None) -> None:
		entity = self.context.create_entity()
		entity.add(Position, x, y)
		entity.add(Image, img)
		entity.add(Clickable)
		if extra_comp: entity.add(extra_comp)
