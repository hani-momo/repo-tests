graph = { # для каждой вершины хранится список ее смежных вершин
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

def bfs(graph, start, visited=[]):
    queue = [start]  # очередь с первой вершиной
    visited.append(start)  # первую вершину посетили

    while queue:  # пока в очереди что-то есть
        node = queue.pop(0)  # новый узел = первый эл из очереди
        for n in graph[node]:  
            if n not in visited:
                visited.append(n)
                queue.append(n)

    return visited

print(bfs(graph, '3'))
