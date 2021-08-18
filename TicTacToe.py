# Exercise 26

def who_wins(matrix):
    # Row winner
    for i in range(len(matrix)):
        if matrix[i] == [1, 1, 1]:
            print('player 1 wins')
        elif matrix[i] == [2, 2, 2]:
            print('player 2 wins')

    # Column winner
    for i in range(len(matrix)):
        if [col[i] for col in matrix] == [1, 1, 1]:
            print("player 1 wins")
        elif [col[i] for col in matrix] == [2, 2, 2]:
            print("player 2 wins")

    # Normal diagonal winner
    if [matrix[i][i] for i in range(len(matrix))] == [1, 1, 1]:
        print("player 1 wins")
    elif [matrix[i][i] for i in range(len(matrix))] == [2, 2, 2]:
        print("player 2 wins")

    # Reversed diagonal winner
    elif [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))] == [1, 1, 1]:
        print("player 1 wins")
    elif [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))] == [2, 2, 2]:
        print("player 2 wins")


who_wins([[1, 2, 0], [2, 1, 0], [2, 1, 0]])
