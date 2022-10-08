class BinarySearchTree:
	def __init__(self, game, depth = 1):
		self.game = game
		self.genre = game[0]
		self.title = game[1]
		self.score = game[2]
		self.plat = game[3]
		self.year = game[4]
		self.depth = depth
		self.right = None
		self.left = None

	def insert(self, game):
		if game[0]<self.genre:
			if self.left == None:
				self.left = BinarySearchTree(game, self.depth+1)
			else:
				self.left.insert(game)
		else:
			if self.right == None:
				self.right = BinarySearchTree(game, self.depth+1)
			else:
				self.right.insert(game)

	def get_game_by_genre(self, genre):
		found_games = []
		if self.genre == genre:
			found_games.append(self)
			if self.right is not None and self.right.genre >= genre:
				return found_games + self.right.get_game_by_genre(genre)
			else:
				return found_games
		elif self.left != None and genre<self.genre:
			return found_games + self.left.get_game_by_genre(genre)
		elif self.right != None and genre>=self.genre:
			return found_games + self.right.get_game_by_genre(genre)
		else:
			return []

	#Inorder traversal
	def print_tree(self):
		if self.left:
			self.left.print_tree()		
		print(f"{self.genre[0:2]} {self.title} at Depth {self.depth}")
		if self.right:
			self.right.print_tree()

	def __repr__(self):
		return str(self.game)