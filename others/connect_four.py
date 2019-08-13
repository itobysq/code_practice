#2033 LEBOWIT

"""
Module for building a connect 4 game 

Connect Four is a game where two players take turns  dropping their color discs into a 
vertically suspended grid. The game ends when a player adds a disc to the playing grid that
connects four discs of their color. The connected discs can be in a horizontal, 
vertical or diagonal line. Write a function to be called after every turn that returns 
true if the game is over (and false otherwise).

[['E' 'B' 'E'],
 ['R' 'B' 'R']
connect 2 - True

[['E', 'E', 'E'],
 ['B', 'R', 'E']]
 connect 2 - False

[['E', 'E', 'E'],
['B', 'R', 'B'],
['R', 'B', 'R'],
connect 3 - false

1. dumb solution 'brute force'
a. scan the board for a red or a black.
b. search all around for an adjacent red or black
c. if we see one, note the direction that the red or black is
d. continue down that direction to see if we get 4

complexity
a. scan is n**2
question: when do you stop??????

a. for each taken piece R/B
b. check every direction and search along that direction
c. if we don't get 4 in every direction
d. change the value to 'e' (remove duplicate work 
e. C = number of things to connect
f. time O (C x N**2)
g. space O(1)

duplicate work - 

To do
a. loop through each taken piece R/B
b. check every direction and search along that direction
    if there is a piece either on horizontal vertical or diaganal, explore
    that path
        recursively call a function check lenght
        base case - no other places to check
        reducing problem - pop a place to check
        if no 
c. if we don't get 4 in every direction
d. change the value to 'e' (remove duplicate work 

assume

"""

def check_board(board, conn=4):
    """
    Args:
        board (list of lists)

    """
    v_edge = len(board) - 1
    h_edge = len(board[0]) - 1

    def explore_surr():

        def on_board(position):
            return (0 <= position[0] < h_edge) and (0 <= position[1] < v_edge)

        def get_next_in_direction(direction, point):
            {'north': (point[0], point[1] + 1),
             'ne': (point[0] + 1, point[1] + 1),
             'east': (point[0] + 1, point[1]),
             'se': (point[0] + 1, point[1] - 1)}
            return point[direction]

        def explore_len(position, direction):
            for move in range(conn) - 1:
                next_point = get_next_in_direction(position, direction)
                if not (on_board(next_point) and board[next_point[0]][next_point[1]] == color):
                    return False
            return True

        card = {'north' : (row_idx, col_idx + 1),
                'ne'  : (row_idx + 1, col_idx + 1),
                'east'  : (row_idx + 1, col_idx),
                'se'  : (row_idx + 1, col_idx - 1)}

        for k,v in card.items()
            if on_board(v) and board[v[0]][v[1]] == color:
                result = explore_len(v, k)
                if result:
                    return True

    for row_idx, row in enumerate(board):
        for col_idx, val in enumerate(row):

            if board[row_idx, col_idx] == 'R' or board[row_idx, col_idx] == 'B':
                cpos = (row_idx, col_idx)
                color = val
                result = explore_surr(cpos)
                if result:
                    return True
    return False

