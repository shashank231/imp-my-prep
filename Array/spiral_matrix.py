# https://leetcode.com/problems/spiral-matrix/submissions/1837044649/


class Solution(object):

    def isValidPosition(self, lx, ly):
        if 0 <= lx <= self.height-1:
            if 0 <= ly <= self.length-1:
                if self.track_visited[lx][ly]==0:
                    return True
        return False

    def fun(self, cd_x, cd_y, index_of_next_move):
        future_posn_x = cd_x + self.order[index_of_next_move][0]
        future_posn_y = cd_y + self.order[index_of_next_move][1]
        valid = self.isValidPosition(future_posn_x, future_posn_y)
        if valid:
            return (True, future_posn_x, future_posn_y)
        return (False, -1, -1)

    def spiralOrder(self, matrix):
        self.order = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.length = len(matrix[0])
        self.height = len(matrix)
        self.track_visited = [[0 for _ in range(self.length)] for _ in range(self.height)]   
        solution = []
        cd_x = 0
        cd_y = 0
        index_of_next_move = 0
        next_move_possible = True

        while next_move_possible:
            # update solution
            solution.append(matrix[cd_x][cd_y])
            # mark visited
            self.track_visited[cd_x][cd_y] = 1

            # check current move good or not
            valid, fx, fy = self.fun(cd_x, cd_y, index_of_next_move)
            if valid:
                cd_x, cd_y = fx, fy
            else:
                # check remaining moves
                moved = False
                for _ in range(3):
                    index_of_next_move = index_of_next_move + 1
                    if index_of_next_move > 3: index_of_next_move = 0
                    valid, fx, fy = self.fun(cd_x, cd_y, index_of_next_move)
                    if valid:
                        moved = True
                        cd_x, cd_y = fx, fy
                        break
                if not moved:
                    # no move possible, we've hit a dead end
                    next_move_possible = False

        return solution


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

o = Solution().spiralOrder(matrix)
print(o)
