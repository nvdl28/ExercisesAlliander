# Exercise 24: Draw A Game Board, part 1 of the tic tac toe exercise

# My solution
def drawgameboard(size):
    if size <= 0:
        print("The size has to be higher than 0")

    elif size == 1:
        print(" --- ")
        print("|   |")
        print(" --- ")

    else:
        for i in range(size):
            print(" --- "*size)
            print("|    "*(size+1))
        print(" --- "*size)


drawgameboard(2)

