class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        if not x and not y:
            return 0

        def knight_moves(coord):
            row, col = coord

            # delta_row = [-1, 0, 1, 0]
            # delta_col = [0, 1, 0, -1]
            delta_row = [-2, -2, -1, -1, 1, 1, 2, 2]
            delta_col = [-1, 1, -2, 2, -2, 2, -1, 1]
            res = []
            for i in range(len(delta_row)):
                move_row = row + delta_row[i]
                move_col = col + delta_col[i]
                res.append((move_row, move_col))
            print(res, len(res))
            return res

        def dfs(starting_node, visited):

            for each_move in knight_moves(starting_node):
                if each_move in visited:
                    continue
                visited.add(each_move)
                dfs(each_move, visited)

        # knight_moves((0,0))
