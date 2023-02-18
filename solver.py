import random

board = [[0 for i in range(9)] for j in range(9)]

def boardinput():
    for row in range(9):
        for col in range(9):
            value = input("Enter value for cell ({},{}): ".format(row, col))
            if value.isdigit() and int(value) in range(0, 10):
                board[row][col] = int(value)
            else:
                print("Invalid input. Please enter a number from 1 to 9, 0 if blank.")
                value = input("Enter value for cell ({},{}): ".format(row, col))
                board[row][col] = int(value)

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def generateRandomBoard(bo):
    find = find_empty(bo)
    if find is None:  # if find != False
        return True
    else:
        row, col = find
    for number in range(1, 10):
        num = random.randint(1, 9)
        if valid(bo, num, (row, col)):
            board[row][col] = num
            if generateRandomBoard(board):
                return True

            board[row][col] = 0
    return False


def removeCells(board,num):
    while num != 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
        num = num - 1


def sudokuMake(board, level):

    generateRandomBoard(board)
    if level == 1:
        removeCells(board,30)
    if level == 2:
        removeCells(board,40)
    if level == 3:
        removeCells(board,55)

choice = input("generate a puzzle or input your own? (1/2) ")

if choice == '1':
    print("\ngenerating...\n")
    level = input("Select a difficulty level from 1-3, with 3 being the hardest. ")

    while level not in ['1', '2', '3']:
        print('\nERROR! please select a number from 1-3\n')
        level = input("Select a difficulty level from 1-3, with 3 being the hardest. ")
    
    level = int(level)
    sudokuMake(board, level)
    print('puzzle generated! consider 0s as empty spaces\n')
    print_board(board)

else:
    print("inputting puzzle")
    boardinput()
    print("here's the board :)\n")
    print_board(board)

solu = input('\nDo you want the solution for this sudoku puzzle? Y/n\n')
solu = solu.lower()

if solu == 'y':
    solve(board)
    print("solving....")
    print("___________________")
    print_board(board)
    print('ta-da!')

else:
    print('thank you for using my program :) \ngood luck on your puzzle!')