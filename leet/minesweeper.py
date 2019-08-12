class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def build_queue(cpos):
            """
            Builds a queue and performs BFS
            """
            adj_spots = gen_adj_spots(cpos)
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

        def get_adj_spots(cpos):
            """
            Get valid, adjacent spots
            """
            adj_spots = []
            h_edge = len(A[0]) - 1
            v_edge = len(A) - 1
            north = (cpos[0], cpos[1] + 1)
            if (0 <= north[0] < h_edge) and (0 <= north[1] < v_edge):
                adj_spots.append(north)
            ne = (cpos[


            
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        else:
            build_queue(click)

        
