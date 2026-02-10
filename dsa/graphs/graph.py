from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)

        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
       
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    

    def __str__(self):
        return str(self.graph)


g = Graph()
print(g)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

print(g)

print("DFS")
print(g.dfs(0, set([])))

print("BFS")
print(g.bfs(0))
