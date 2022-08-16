import arcade
from entitas import *
from Component import *

sprites = {}
class CreateSprite(ReactiveProcessor):
	def __init__(self, context: Context):
		super().__init__(context)

	def get_trigger(self):
		return {Matcher(Image): GroupEvent.ADDED}
	
	def filter(self, entity):
		return entity.has(Image) and not entity.has(Sprite)

	def react(self, entities):
		for e in entities:
			sprite = arcade.Sprite(e.get(Image).source)
			sprites[sprite] = e
			e.add(Sprite, sprite)
			if e.has(Position): e.replace(Position, e.get(Position).x, e.get(Position).y)
			if e.has(Scale): e.replace(Scale, e.get(Scale).scale)

class RemoveSprite(ReactiveProcessor):
	def __init__(self, context: Context):
		super().__init__(context)

	def get_trigger(self):
		return {Matcher(Image): GroupEvent.REMOVED}
	
	def filter(self, entity):
		return not entity.has(Image);

	def react(self, entities):
		for e in entities:
			del sprites[e.get(Sprite)]
			e.remove(Clickable)
			e.remove(Sprite)

class RenderSprite(ExecuteProcessor):
	def __init__(self, context: Context):
		super().__init__()
		self.context = context
		self.group = context.get_group(Matcher(Sprite))

	def execute(self):
		arcade.start_render()
		for e in self.group.entities:
			e.get(Sprite).sprite.draw()

class UpdatePosition(ReactiveProcessor):
	def __init__(self, context: Context):
		super().__init__(context)

	def get_trigger(self):
		return {Matcher(Position): GroupEvent.ADDED}
	
	def filter(self, entity):
		return entity.has(Position, Sprite)

	def react(self, entities):
		for e in entities:
			pos = e.get(Position)
			sprite = e.get(Sprite).sprite
			sprite.center_x = pos.x
			sprite.center_y = pos.y

class UpdateScale(ReactiveProcessor):
	def __init__(self, context: Context):
		super().__init__(context)

	def get_trigger(self):
		return {Matcher(Scale): GroupEvent.ADDED}
	
	def filter(self, entity):
		return entity.has(Scale, Sprite)

	def react(self, entities):
		for e in entities:
			e.get(Sprite).sprite.scale = e.get(Scale).scale

clickables = arcade.SpriteList(True)
class AddClickable(ReactiveProcessor):
	def __init__(self, context: Context):
		super().__init__(context)

	def get_trigger(self):
		return {Matcher(Clickable): GroupEvent.ADDED}
	
	def filter(self, entity):
		return entity.has(Clickable, Sprite)

	def react(self, entities):
		for e in entities:
			clickables.append(e.get(Sprite).sprite)

class RemoveClickable(ReactiveProcessor):
	def __init__(self, context: Context):
		super().__init__(context)

	def get_trigger(self):
		return {Matcher(Clickable): GroupEvent.REMOVED}
	
	def filter(self, entity):
		return not entity.has(Clickable) and entity.has(Sprite)

	def react(self, entities):
		for e in entities:
			clickables.remove(e.get(Sprite).sprite)

class UpdateClicked(ExecuteProcessor):
	def __init__(self, context: Context):
		super().__init__()
		self.context = context
		self.cgroup = context.get_group(Matcher(Cursor))

	def update(self, x, y):
		for c in self.cgroup.entities:
			cs = c.get(Sprite).sprite
			m = arcade.check_for_collision_with_list(cs, clickables)
			for s in m:
				e = sprites[s]
				if e.has(Clicked):
					print("Clicked twice in a single frame")
					continue
				e.add(Clicked)
				print(f"{e} is clicked")

	def execute(self):
		pass

class CleanupClicked(CleanupProcessor):
	def __init__(self, context: Context):
		super().__init__()
		self.context = context
		self.group = context.get_group(Matcher(Clicked))

	def cleanup(self):
		while len(self.group.entities) > 0:
			self.group.entities.pop().remove(Clicked)

class CreateCursor(InitializeProcessor):
	def __init__(self, context: Context):
		super().__init__()
		self.context = context

	def initialize(self):
		entity = self.context.create_entity()
		entity.add(Position, 0, 0)
		entity.add(Scale, 0.25)
		entity.add(Image, "assets/default/cursor.png")
		entity.add(Cursor)

class UpdateMousePosition(ExecuteProcessor):
	def __init__(self, context: Context):
		super().__init__()
		self.context = context
		self.group = context.get_group(Matcher(Cursor))

	def update(self, x, y):
		for e in self.group.entities:
			e.replace(Position, x, y)

	def execute(self):
		pass
