import arcade
from entitas import *
from GenericProc import *
from MenuProc import *

class MainView(arcade.View):
	def __init__(self) -> None:
		super().__init__()

		self.context = context = Context()
		self.processors = processors = Processors()

		self.mouse_motion_processor = UpdateMousePosition(context)
		processors.add(self.mouse_motion_processor)
		self.mouse_press_processor = UpdateClicked(context)
		processors.add(self.mouse_press_processor)

		processors.add(CreateSprite(context))
		processors.add(RemoveSprite(context))
		processors.add(UpdatePosition(context))
		processors.add(UpdateScale(context))

		processors.add(RenderSprite(context))
		
		processors.add(CreateCursor(context))
		processors.add(CreateMenuButtons(context))

		processors.activate_reactive_processors()
		processors.initialize()

	def on_update(self, delta_time: float) -> None:
		self.processors.execute()
		self.processors.cleanup()

	def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
		self.mouse_motion_processor.update(x, y)

	def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
		self.mouse_press_processor.update(x, y)