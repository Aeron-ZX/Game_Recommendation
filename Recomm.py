from gamesData import games, add_game
from BinarySearchTree import *

# print("""Hi there. You can use this little program to get a recommendation of a videogame. 
#  The results are based on a small selection of some of the highest scoring titles of the website Metacritic.
#  Metacritic is a review aggregator for entertainment products (films, music, videogames, books...). Each product
#  has an average based on critics' scores and another based from users' scores.
#  The games selected try to range from different platforms and year of publication. The bare minimum is a score of 80
#  points from critics.""")
# choice = input("Now then, type the beginning of the genre you'd like to play and let's see what we have ")

test = BinarySearchTree(games[0])
print(test)