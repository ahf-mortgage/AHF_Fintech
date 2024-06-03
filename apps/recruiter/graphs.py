from .models import MLONode


def dfs(start_node):
 
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node
            stack.extend(node.neighbors.all())

def bfs(start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            yield node
            queue.extend(node.neighbors.all())
            
            
