import pprint

# solve.py
def solve(su):
    

    """
    Solves a sudoku board using backtracking
    :param su:2nd list of ints
    :return: solution
    """

    
    find = find_empty(su)
    if find:
        row,col = find
    else:
        return True

    for i in range(1,10):
        if valid(su,(row,col), i):
            su[row][col] = i

            if solve(su):
                return True

            su[row][col] = 0

    return False


def valid(su, pos, num):
    """
    Returns if the attempted move is valid
    :param su: 2nd list of ints
    :param pos:(row, col)
    :param num: int
    :return: bool
    """
        

    # check row
    for i in range(0, len(su)):
        if su[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(0, len(su)):
        if su[i][pos[1]] == num and pos[1] !=i:
            return False   

    #  check box

    box_x = pos[1]//3
    box_y = pos[0]//3
        
    for i in range(box_y*3, box_y*3 ==3):
        for j in range(box_x*3, box_x*3  == 3):
            if su[i][j] == num and (i,j) !=pos:
                return False

        return True

def find_empty(su):
    """
    finds an empty space  in the board
    :param su:partially complete board
    :return: (int, int) row col 
    """
    


    for i in range(len(su)):
        for j in range(len(su[0])):
            if su[i][j] == 0:
                return (i, j)
    return None  


def print_board(su):
    """
    prints the board
    :param su: 2nd list of ints 
    :returns: None
    """

    for i in range(len(su)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        for j in range(len(su[0])):
            if j % 3 == 0:
                print("|",end="")    

            if j == 8:
                print(su[i][j],end="\n")
            else:
                print(str(su[i][j]) + " ", end="")

board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,8,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
]  

pp = pprint.PrettyPrinter(width=41, compact=True)
solve(board)
pp.pprint(board)