def dfs(graph, start):
    # Проверяем, существуют ли вершины a и b в графе
    if a not in graph or b not in graph:
        raise ValueError("Некорректные вершины a или b")
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))  # для корректного порядка
    return visited

def dfs_path_length(graph, a, b):
    if a == b:
        return 0
    visited = {}
    stack = [(a, 0)]
    while stack:
        node, depth = stack.pop()
        if node == b:
            return depth
        if node not in visited:
            visited[node] = True
            for neighbor in reversed(graph[node]):
                stack.append((neighbor, depth + 1))
    return -1  # если путь не найден

# Пример использования
if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = {}
    for a, b in edges:
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    print(dfs(graph, 1))  # Вывод: [1, 3]
    print(dfs_path_length(graph, 2, 4))  # Вывод: 1