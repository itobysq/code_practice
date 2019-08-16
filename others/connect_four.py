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
    v_edge = len(board)
    h_edge = len(board[1])

    def explore_surr(row_idx, col_idx, color):

        def on_board(position):
            return (0 <= position[1] < h_edge) and (0 <= position[0] < v_edge)

        def explore_len(position, direction):
            print('exploring the length')
            for move in range(conn - 1):
                print('another one')
                next_point = get_next_in_direction(position, direction)
                if not (on_board(next_point) and board[next_point[0]][next_point[1]] == color):
                    return False
            return True

        def recurs(n_in_a_row, conn, point):
            print('exploring the length')
            next_points = {'north': (point[0] + 1, point[1]),
                            'ne': (point[0] + 1, point[1] + 1),
                            'east': (point[0], point[1] + 1),
                            'se': (point[0] - 1, point[1] + 1)}
            if n_in_a_row == conn:
                return True
            else:
                if on_board(point) and board[point[0]][point[1]] == color:
                    print('another one')
                    n_in_a_row += 1
                    return recurs(n_in_a_row, conn, point)

        card = {'north' : (row_idx + 1, col_idx),
                'ne'  : (row_idx + 1, col_idx + 1),
                'east'  : (row_idx , col_idx + 1),
                'se'  : (row_idx - 1, col_idx + 1)}

        for k,v in card.items():
            print('exploring adjacent piece {}, {}'.format(k, v))
            n_in_a_row = 1
            if on_board(v) and board[v[0]][v[1]] == color:
                n_in_a_row += 1
                res = recurs(n_in_a_row, conn, (row_idx, col_idx))
                if res:
                    return True


    for row_idx, row in enumerate(board):
        for col_idx, val in enumerate(row):
            print('inspecting {0}, {1}, color is {2}'.format(row_idx,
                                                              col_idx,
                                                              board[row_idx][col_idx]))


            if board[row_idx][col_idx] == 'R' or board[row_idx][col_idx] == 'B':
                print('piece is colored')
                color = val
                result = explore_surr(row_idx, col_idx, color)
                if result:
                    return True
    return False
if __name__ == '__main__':
    board = [['E', 'B', 'E'],
            ['R', 'B', 'R']]
    res = check_board(board, conn=2)
    assert res
    board = [['E', 'E', 'E'],
            ['R', 'B', 'R']]
    res = check_board(board, conn=2)
    assert not res
