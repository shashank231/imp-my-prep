import pdb
from pprint import pprint
from collections import defaultdict
from typing import List


class Solution1:

    def return_gph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return dict(graph)

    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        graph = self.return_gph(edges)
        visited = set()
        solution = False

        def dfs(node):
            nonlocal solution
            if node==destination:
                solution = True
                return
            if node in visited:
                return            
            visited.add(node)
            for nbr in graph.get(node, []):
                dfs(nbr)

        dfs(source)
        return solution


class Solution2:
    mem = {}

    def setChessBoard(self, n):
        mat = []
        for i in range(n):
            mat.append([0 for j in range(n)])
        self.chessBoard = mat

    def isvalidPosition(self, i, j, n):
        if i < 0 or j < 0:
            return False
        if i >= n or j >= n:
            return False
        return True
    
    def returnPossiblePositions(self, i, j, n):
        possiblePositions = []
        moves = [
            (2, 1),
            (2, -1),
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
            (-2, -1),
            (-2, 1),
        ]
        for mv in moves:
            new_posn_i = i + mv[0]
            new_posn_j = j + mv[1]
            if self.isvalidPosition(new_posn_i, new_posn_j, n):
                possiblePositions.append(
                    (new_posn_i, new_posn_j)
                )
        return possiblePositions
    
    def findMinMoves(self, current_i, current_j, n):
        g1 = self.mem.get((current_i, current_j))
        if g1:
            return g1

        if current_i == self.dest_i and current_j == self.dest_j:
            return 0
        self.chessBoard[current_i][current_j] = 2
        possibleNextPositions = self.returnPossiblePositions(current_i, current_j, n)
        actualPositionsToConsider = []
        for p in possibleNextPositions:
            if self.chessBoard[p[0]][p[1]] == 2:
                continue
            else:
                actualPositionsToConsider.append(p)

        minMoves = float("inf")
        for p in actualPositionsToConsider:
            moves = 1 + self.findMinMoves(p[0], p[1], n)
            minMoves = min(moves, minMoves)

        self.chessBoard[current_i][current_j] = 0
        self.mem.update({(current_i, current_j): minMoves})
        return minMoves

    def minStepToReachTarget(self, knightPos, targetPos, n):
        self.setChessBoard(n)
        self.dest_i = targetPos[0] - 1
        self.dest_j = targetPos[1] - 1
        return self.findMinMoves(
            knightPos[0]-1,
            knightPos[1]-1,
            n,
        )
# ans = Solution2().minStepToReachTarget([4, 5], [1, 1], 6)
# print(ans)


class Solution3:
    answer = 0
    directed_graph = defaultdict(list)
    all_neighbours_graph = defaultdict(list)

    def make_graphs(self, conns):
        for con in conns:
            self.directed_graph[con[0]].append(con[1])
            self.all_neighbours_graph[con[0]].append(con[1])
            self.all_neighbours_graph[con[1]].append(con[0])

    def main(self):
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            directed_connections = self.directed_graph.get(node, [])
            all_neighbours = self.all_neighbours_graph.get(node, [])
            need_to_reverse = directed_connections
            for j in need_to_reverse:
                if j not in visited:
                    # print(node, need_to_reverse)
                    self.answer += 1
            for neighbour in all_neighbours:
                if neighbour not in visited:
                    dfs(neighbour)
        dfs(0)

    def minReorder(self, n: int, connections) -> int:
        self.make_graphs(connections)
        self.main()
        return self.answer
# ans = Solution3().minReorder(5, [[1,0],[1,2],[3,2],[3,4]])
# print(ans)


class Solution4:

    def set_graph_dict(self, conns):
        self.graph_dict = defaultdict(list)
        for i in range(len(conns)):
            con = conns[i]
            for ele in con:
                self.graph_dict[i].append(ele)

    def main(self):
        self.answer = list()
        visited = set()
        recStack = []

        def dfs(node) -> bool:
            if node in recStack:
                return False
            if node in visited:
                return self.mem.get(node)
 
            visited.add(node)
            recStack.append(node)
            
            isTerminalNode = not self.graph_dict.get(node)
            if isTerminalNode:
                self.answer.append(node)
                self.mem.update({node: True})
                recStack.remove(node)
                return True

            isSafenode = True
            for neighbour in self.graph_dict.get(node):
                isNeighbourSafeNode = dfs(neighbour)
                isSafenode = isSafenode and isNeighbourSafeNode

            if isSafenode:
                self.answer.append(node)
            
            self.mem.update({node: isSafenode})
            recStack.remove(node)
            return isSafenode

        for nd in range(self.num1):
            if nd not in visited:
                dfs(nd)
 
    def eventualSafeNodes(self, graph):
        self.num1 = len(graph)
        self.mem = {}
        self.set_graph_dict(graph)
        self.main()
        return sorted(self.answer)
# s1 = Solution4().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
# print("s1 => ", s1)


class Solution5:
    
    def main(self):
        visited = set()
        visited_at = {}  # node -> index when it was visited in this path
        max_length_of_cycle = -1

        def dfs(node, step):
            nonlocal max_length_of_cycle

            if node in visited:
                return

            visited_at[node] = step
            visited.add(node)

            nbr = self.edges[node]
            if nbr != -1:
                if nbr not in visited:
                    dfs(nbr, step + 1)
                elif nbr in visited_at:
                    # found a cycle → length = current step - entry step of neighbor + 1
                    cycle_length = step - visited_at[nbr] + 1
                    max_length_of_cycle = max(max_length_of_cycle, cycle_length)

            # clean up this node's entry for future paths
            visited_at.pop(node)

        for node in range(self.gphN):
            if node not in visited:
                dfs(node, 0)

        return max_length_of_cycle

    def longestCycle(self, edges: List[int]) -> int:
        self.edges = edges
        self.gphN = len(edges)
        return self.main()
# s1 = Solution5().longestCycle([2,-1,3,1])
# print(s1)


class Solution6:
    def set_graph(self, prerequisites):
        self.graph_dict = defaultdict(list)
        for req in prerequisites:
            self.graph_dict[req[1]].append(req[0])

    def main(self, numCourses: int):
        visited = set()
        t_sort_reverse = []
        rec_stack = set()
        cycle = False

        def dfs(node):
            nonlocal cycle
            if node in rec_stack:
                cycle = True
                return
            if node in visited:
                return
            visited.add(node)
            rec_stack.add(node)
            for nbr in self.graph_dict.get(node, []):
                dfs(nbr)
            rec_stack.remove(node)
            t_sort_reverse.append(node)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)

        if cycle:
            return []
        return t_sort_reverse[::-1]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.set_graph(prerequisites)
        return self.main(numCourses)
# s1 = Solution6().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
# print(s1)



class Solution:
    
    def set_graph(self, edges):
        self.gph = defaultdict(list)
        for edge in edges:
            self.gph[edge[0]].append(edge[1])

    def get_probable_solution(self, nodes, colors):
        colors_dict = dict()
        for node in nodes:
            colour_of_node = colors[node]
            colors_dict[colour_of_node] = colors_dict.setdefault(colour_of_node, 0) + 1
        max_times = 0
        for k, v in colors_dict.items():
            max_times = max(max_times, v)        
        return max_times

    def main(self, colours):
        visited = set()
        recStack = []
        solution = -1
        isCyclic = False

        def dfs(node):
            nonlocal isCyclic
            nonlocal solution

            if not self.gph[node]:
                recStack.append(node)
                visited.add(node)
                probable_solution = self.get_probable_solution(recStack, colours)
                solution = max(solution, probable_solution)
                recStack.pop()
                return

            if node in recStack:
                isCyclic = True
                return
            
            visited.add(node)
            recStack.append(node)
            for nbr in self.gph[node]:
                dfs(nbr)
            recStack.pop()
        
        for node in range(len(colours)):
            if node not in visited:
                dfs(node)
        
        if isCyclic:
            return -1
        
        return solution

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        self.set_graph(edges=edges)
        return self.main(colors)



a = Solution().largestPathValue("nnllnzznn", [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]])
print(a)


