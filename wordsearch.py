"""
Introduction to Programming: Coursework 1
Please write your name
@author:louis bishop (i dont do the module i just did this for giggles)
"""

# Reminder: You are not allowed to import any modules.

def wordsearch(puzzle: list, wordlist: list) -> None:
    # delete pass to write your code
    pass


def valid_puzzle(puzzle: list) -> bool:
    valid = True
    for x in puzzle:
        if len(x) != len(puzzle[0]):
            valid = False
        for y in x:
            if y.isdigit():
                valid = False
    return valid


def valid_wordlist(wordlist: list) -> bool:
    valid = True
    for x in wordlist:
        if isinstance(x,int):
            valid = False
    return valid
            


def get_positions(puzzle: list, word: str) -> list:
    letterToSearch = word[0] #store the first letter of the word
    listOfStarts = [] #array to store the list of starting letters (if any)
    currentRow = 0 #keep track of where is being observed
    currentColumn = 0
    coordinateList = [] #list of coordinates for the word letter locations
    for x in puzzle: #for every row:
        for y in x: #for every letter in every row:
            if y == letterToSearch: #if the letter is an instance of the first letter
                listOfStarts.append((currentRow,currentColumn)) #add the coordinates being observed to the list of starts
            currentColumn = currentColumn + 1 #move to the next column
        currentRow = currentRow + 1 #move to the next row
        currentColumn = 0 #back to the first column
    if len(listOfStarts) == 0:
        print(word + " not found.") #if you dont find any starts it's not there!
        return 0
    else:
        for x in listOfStarts:
            valid = True
            #left
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchColumn < 0:
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    valid = False
                    coordinateList.clear()
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchColumn = searchColumn - 1
            if valid == True:
                break
            valid = True
            #left-up
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchColumn < 0 or searchRow < 0:
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    coordinateList.clear()
                    valid = False
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchColumn = searchColumn - 1
                    searchRow = searchRow - 1
            if valid == True:
                break
            valid = True
            #up
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchRow < 0:
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    valid = False
                    coordinateList.clear()
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchRow = searchRow - 1
            if valid == True:
                break
            valid = True
            #up-right
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchColumn > (len(puzzle[0])-1) or searchRow < 0:
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    valid = False
                    coordinateList.clear()
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchColumn = searchColumn + 1
                    searchRow = searchRow - 1
            if valid == True:
                break
            valid = True
            #right
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchColumn > (len(puzzle[0])-1):
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    valid = False
                    coordinateList.clear()
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchColumn = searchColumn + 1   
            if valid == True:
                break
            valid = True
            #down-right
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchColumn > (len(puzzle[0])-1) or searchRow > (len(puzzle)-1):
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    valid = False
                    coordinateList.clear()
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchColumn = searchColumn + 1
                    searchRow = searchRow + 1
            if valid == True:
                break
            valid = True
            #down
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchRow > (len(puzzle)-1):
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    valid = False
                    coordinateList.clear()
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchRow = searchRow + 1
            if valid == True:
                break
            valid = True
            #down-left
            searchRow = x[0]
            searchColumn = x[1]
            for y in word:
                if searchColumn < 0 or searchRow > (len(puzzle)-1):
                        valid = False
                        coordinateList.clear()
                        break
                if y != puzzle[searchRow][searchColumn]:
                    valid = False
                    coordinateList.clear()
                    break
                else:
                    coordinateList.append((searchRow,searchColumn))
                    searchColumn = searchColumn - 1
                    searchRow = searchRow + 1    
            if valid == True:
                break
        if valid == False:
            print(word + " not found.")
        else:
            print(word + " found.")
            print("In the format (ROW, COLUMN):")
            return coordinateList
            
            
def basic_display(grid: list) -> None:
    newLineCounter = 0
    for x in grid:
        for y in x:
            print(y,end = " ")
        print(" ")


def coloured_display(grid: list, positions: list) -> None:
    # delete pass to write your code
    pass


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    #test_valid_puzzle()
    #test_valid_wordlist()
    test_basic_display()

    # full solution
    # test_coloured_display()
    test_get_positions()
    # test_wordsearch()
