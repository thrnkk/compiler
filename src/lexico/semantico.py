from .constants import Constants
from .lexical_error import LexicalError

class Semantico(Constants):

	def __init__(self):

		Constants.__init__(self)

		def executeAction(self, action, token):

			print(f"Ação #{action}, Token: {token}")
