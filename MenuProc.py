import arcade
from entitas import *
from Component import *
from Consts import *

class CreateMenuButtons(InitializeProcessor):
	def __init__(self, context: Context):
		super().__init__()
		self.context = context

	def initialize(self) -> None:
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 + 5 * 32, 1, "assets/menu/start.png")
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 + 2 * 32, 2, "assets/menu/setting.png")
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 - 1 * 32, 3, "assets/menu/mapedit.png")
		self.create_button(SCREEN_W / 2, SCREEN_H / 2 - 4 * 32, 4, "assets/menu/quit.png")
		self.create_button(96, 32, 0, "assets/menu/back.png")

	def create_button(self, x, y, id, img) -> None:
		entity = self.context.create_entity()
		entity.add(Position, x, y)
		entity.add(Image, img)
		entity.add(Clickable)
		entity.add(MenuButton, id)

class OnMenuButtonClicked(ReactiveProcessor):
	def __init__(self, context: Context):
		super().__init__(context)

	def get_trigger(self):
		return {Matcher(Clicked): GroupEvent.ADDED}
	
	def filter(self, entity):
		return entity.has(Clicked, MenuButton)

	def react(self, entities):
		e = entities[0]
		match e.get(MenuButton).id:
			case 0 | 4: # Back / Quit
				arcade.close_window()
				quit()
			case 1: # Start
				pass
			case 2: # Settings
				pass
			case 3: # Map Edit
				pass
