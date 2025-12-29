from typing import List
from collections import defaultdict


class TaskGraph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_task(self, task_name: str, dependencies: List[str]):
        self.graph[task_name].extend(dependencies)

    def get_execution_order(self):
        visited = set()
        topological_sort = list()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            dependencies = self.graph[node]
            for dependency in dependencies:
                dfs(dependency)
            topological_sort.append(node)

        for node in self.graph.keys():
            if node not in visited:
                dfs(node)

        return topological_sort


graph = TaskGraph()
graph.add_task("build_index", ["extract", "transform"])
graph.add_task("extract", [])
graph.add_task("transform", ["extract"])
graph.add_task("load", ["build_index"])

print(graph.get_execution_order())