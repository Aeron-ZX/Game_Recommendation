from gamesData import games, add_game
from BinarySearchTree import *

# print("""Hi there. You can use this little program to get a recommendation of a videogame. 
#  The results are based on a small selection of some of the highest scoring titles of the website Metacritic.
#  Metacritic is a review aggregator for entertainment products (films, music, videogames, books...). Each product
#  has an average based on critics' scores and another based from users' scores.
#  The games selected try to range from different platforms and year of publication. The bare minimum is a score of 80
#  points from critics.""")
# choice = input("Now then, type the beginning of the genre you'd like to play and let's see what we have ")

games.sort()

# test = BinarySearchTree(games[0])
# for i in range(1, len(games)):
#     test.insert(games[i])


# def heapify(lst):
#     mid = len(lst)//2
#     #BST = BinarySearchTree(lst.pop(mid))
#     print(lst.pop(mid))
#     print(lst)
#     while lst != []:
#         left = lst[0:mid]
#         mid_left = len(left)//2
#         right = lst[mid:]
#         mid_right = -len(right)//2
#         print(lst.pop(mid_left))
#         print(lst)
#         if lst == []:
#             continue
#         print(lst.pop(mid_right))
#         print(lst)
#         mid = len(lst)//2 -1 
#     return lst


# Recursive function to sort an array so the elements can be inserted into a balanced BinarySearchTree
def sorted_array_to_bst(lst, BST = None):
    if lst == []:
        return BST
    mid = len(lst)//2
    if BST == None:
        BST = BinarySearchTree(lst.pop(mid))
    else:
        BST.insert(lst.pop(mid))
    left = sorted_array_to_bst(lst[0:mid], BST)
    right = sorted_array_to_bst(lst[mid:], BST)
    return left and right


BST = sorted_array_to_bst(games)
print(BST)

print(BST.get_game_by_genre("adventure"))



# def heapify(lst, BST):
#     if lst == []:
#         return 
#     mid = len(lst)//2
#     print(lst.pop(mid))
#     left = heapify(lst[0:mid], BST)
#     right = heapify(lst[mid:], BST)
#     return left
