def updateBoard(board, click):
    def get_adj_spots(cpos):
        """
        Get valid, adjacent spots
        """
        adj_spots = []
        h_edge = len(A[0]) - 1
        v_edge = len(A) - 1

        def check_borders(point):
            if (0 <= point[0] < h_edge) and (0 <= point[1] < v_edge):
                adj_spots.append(point)

        north = (cpos[0], cpos[1] + 1)
        check_borders(north)

        ne = (cpos[0] + 1, cpos[1] + 1)
        check_borders(ne)

        east = (cpos[0] + 1, cpos[1])
        check_borders(east)

        se = (cpos[0] + 1, cpos[1] - 1)
        check_borders(se)

        south = (cpos[0], cpos[1] - 1)
        check_borders(south)

        sw = (cpos[0] - 1, cpos[1] - 1)
        check_borders(south)

        west = (cpos[0] - 1, cpos[1])
        check_borders(west)

        nw = (cpos[0] - 1, cpos[1] + 1)
        check_borders(nw)

    def build_queue(cpos):
        """
        Builds a queue and performs BFS
        """
        print('current position is cpos'.format(cpos))
        print('building up the queue of places to visit')
        adj_spots = gen_adj_spots(cpos)
        print('ques is {}'.format(queue))
        val = 0
        queue = []
        for spot in adj_spots:
            if board[spot[0]][spot[1]] == 'M':
                val += 1

            elif board[spot[0]][spot[1]] == 'E':
                queue.append(spot)

        if val > 0:
            board[cpos[0]][cpos[1]] = str(val)
        else:
            board[cpos[0]][cpos[1]] = 'B'

        for dest in queue:
            build_queue(dest)



    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
    else:
        build_queue(click)
    return board

if __name__ == '__main__':
    board = [['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']]
    click = [1,2]

    answer = [['B', '1', 'E', '1', 'B'],
            ['B', '1', 'X', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']]

    result = updateBoard(board, click)

    assert answer == result

    board2 = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

    ans2 = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
    click2 = [3,0]
    res2 = updateBoard(board2, click2)
    assert ans2 == res2
