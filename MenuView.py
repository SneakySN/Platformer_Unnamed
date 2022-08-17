import arcade
from entitas import *
from GenericProc import *
from MenuProc import *
from BaseView import *

class MenuView(BaseView):
	def setup_processors(self, processors, context) -> None:
		processors.add(OnMenuButtonClicked(context))

		processors.add(CreateCursor(context))
		processors.add(CreateMenuButtons(context))
