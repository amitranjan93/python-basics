# graphs
# BFS → Queue → level by level
# DFS → Stack → depth first

from collections import deque
def bfs(graph, start,parent):
    queue = deque([start])
    visited = {start}
    result = []
    while(queue):
        node = queue.popleft()
        for item in graph[node]:
            if item not in visited:
                queue.append(item)
                parent[item] = node
                visited.add(item)
        result.append(node)
    return result

def reconstruct_path(parent, start, target):
    path = []
    current = target
    path.append(current)
    while(current != start):
        if current not in parent:
            return -1
        path.append(parent[current])
        current = parent[current]

    return path[::-1]

def has_path(graph, start, target):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()

        if node == target:
            return True

        if node not in graph:
            continue

        for item in graph[node]:
            if item not in visited:
                visited.add(item)
                queue.append(item)

    return False

def dfs(graph, start):
    stack = [start]
    visited = {start}
    result = []
    while stack:
        node = stack.pop()
        for item in graph[node]:
            if item not in visited:
                stack.append(item)
                visited.add(item)
        result.append(node)
    return result

def has_cycle(graph):
    visited = set()
    stack = []
    for item in graph:
        if item not in visited:
            visited.add(item)
            stack.append((item,None))
        while stack:
            node,parent = stack.pop()
            for item in graph[node]:
                if item in visited and parent != item:
                    return True
                if item not in visited:
                    stack.append((item,node))
                    visited.add(item)
    return False

def has_cycle_dfs(graph):
    visited = set()
    current_path = set()

    def dfs(node):
        visited.add(node)
        current_path.add(node)

        for neighbour in graph[node]:

            # Back to a node in the current DFS path → cycle
            if neighbour in current_path:
                return True

            # Not explored before → explore deeper
            if neighbour not in visited:
                if dfs(neighbour):
                    return True

        # Finished exploring this node
        current_path.remove(node)
        return False

    # Handle disconnected components
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


def topological_sort(graph):

    # Step 1: Calculate indegree
    indegree = {}

    for node in graph:
        indegree[node] = 0

    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    # Step 2: Put all nodes with indegree 0 into queue
    queue = deque()

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    # Step 3: Process the queue
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Step 4: Remove outgoing edges
        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            # Step 5: If indegree becomes 0, add to queue
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    if len(result) != len(graph):
        return []   

    return result

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print(topological_sort(graph))
