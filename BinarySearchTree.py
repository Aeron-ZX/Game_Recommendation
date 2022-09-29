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

	def __repr__(self):
		return str(self.game)