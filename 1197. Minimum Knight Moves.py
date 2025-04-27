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
            # print(res, len(res))
            return res
        # min_count = []
        # min_count[0] = float('inf')
        all_path = []
        # visited = set([starting_node])
        def dfs(starting_node, target_node, visited, path):
            if abs(starting_node[0]) * abs(starting_node[1]) > abs(target_node[0]) * abs(target_node[1]):
                return

            if starting_node == target_node:
                print("found it!")
                #update min_count here:
                # if min_count > len(path[:]):
                #     min_count = len(path[:])
                return
            # exit()
            for each_move in knight_moves(starting_node):
                # exit()
                if each_move in visited:
                    continue
                # print("each_move", each_move)
                visited.add(each_move)
                path.append(each_move)
                # print(visited)
                # exit()
                dfs(each_move,target_node, visited, path)
                path.pop()
                # exit()

        # knight_moves((0,0))
        target_node = (x, y)
        starting_node = (0,0)
        # knight_moves(starting_node)
        dfs(starting_node, target_node, set(), [])
