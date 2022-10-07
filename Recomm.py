from gamesData import games, add_game, genres
from BinarySearchTree import *

#Introduction
print("""Hi there. You can use this little program to get a recommendation of a videogame. 
 The results are based on a small selection of some of the highest scoring titles of the website Metacritic.
 Metacritic is a review aggregator for entertainment products (films, music, videogames, books...). Each product
 has an average based on critics' scores and another based from users' scores.
 The games selected try to range from different platforms and year of publication. The bare minimum is a score of 80
 points from critics.
 When showing the platform '+m' means that this game is multiplatform. The score shown belongs to the platform presented,
 while other versions of this game in other platforms, may have separated scores.
 \n""")

#This function is used to prompt the user to enter the characters to make the search
def ask_genre():
    choice = input("Now then, type the beginning of the genre you'd like to play and let's see what we have\n \n")
    return choice

#This function will prompt the user to confirme the selected genre
def confirm(choice):
    confirmation = input(f"\nThe only option with these letters is {choice.title()}. Do you want to look at {choice.title()} games? Press 'y' for yes and 'n' for no ")
    while confirmation not in ["y", "n"]:
        confirmation = input("Please, press 'y' or 'n' only ")
    if confirmation == "y":
        return choice
    if confirmation == "n":
        return confirmation

#This function crosses the user choice with the list of genres available
def check_genres(choice, genres):
    found_options = []
    for genre in genres:
        if genre.startswith(choice):
            found_options.append(genre)
    if found_options == []:
        choice = input("""\nNo matching genre has been found with these letters. If you don't know what you are looking for, 
some of the most popular genres are 'adventure', 'action' or 'rpg'. Now try again\n 
\n""")
        check_genres(choice, genres)
    elif len(found_options) == 1:
        confirmed_choice = confirm(found_options[0])
        if confirmed_choice == "n":
            check_genres(ask_genre(), genres)
        else:
            print_games(confirmed_choice)
    else:
        print(f"\nWith these beginning letters you may select between these genres: {str(found_options)}")
        print("\n")
        check_genres(ask_genre(), genres)

#This function prints the different games and their attributes, looking through the BST for the genre of choice
#After that prompts the user to make another search or ending the program
def print_games(genre):
    games_to_print = BST.get_game_by_genre(genre)
    for game in games_to_print:
        print(f"""
            --------------------------------------------------

            {game.title}
            Main genre: {game.genre.title()}
            Score: {game.score}
            Platform: {game.plat}
            Year of release: {game.year}
                    """)
    again = input("Would you like to make another search? y/n ")
    while again not in ["y", "n"]:
        again = input("Please, press 'y' or 'n' only ")
    if again == "y":
        check_genres(ask_genre(), genres)
    if again == "n":
        print("We hope you enjoy these games!")


#We use te build-in sort function to order the array by alphabetical order. 
#The list is composed of other lists, which their first element is the genre of the game
games.sort()

#This code creats a BST and insert all the elements of the list into the BST. 
#This will make and unbalanced tree with a lot of depth. In the case that the list is sorted, the BST will become de facto a linked list
# test = BinarySearchTree(games[0])
# for i in range(1, len(games)):
#     test.insert(games[i])


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

#We create our BinarySearchTree (BST) with the sorted list of games. 
#The previous function takes the job of inserting each game into the tree
BST = sorted_array_to_bst(games)


#This call of the check_genres() function will set all in action to start the search with all user prompts, 
#make successive searchs or stop the program
check_genres(ask_genre(), genres)




#The following code has been used for testing or has scarp value. Ignore

#BST.print_tree()
#print(BST.get_game_by_genre("adventure"))

# def heapify(lst, BST):
#     if lst == []:
#         return 
#     mid = len(lst)//2
#     print(lst.pop(mid))
#     left = heapify(lst[0:mid], BST)
#     right = heapify(lst[mid:], BST)
#     return left
