def longest_path(graph: list) -> int:

  def topological_sort(graph):

    n = len(graph)

    in_degree = [0] * n

    for u in range(n):

      for v, _ in graph[u]:

        in_degree[v] += 1

    stack = [i for i in range(n) if in_degree[i] == 0]

    topo_order = []

    while stack:

      u = stack.pop()

      topo_order.append(u)

      for v, _ in graph[u]:

        in_degree[v] -= 1

        if in_degree[v] == 0:

          stack.append(v)

    return topo_order

  def longest_path(graph, topo_order):

    n = len(graph)

    dist = [0] * n

    for u in topo_order:

      for v, w in graph[u]:

        if dist[u] + w > dist[v]:

          dist[v] = dist[u] + w

    return max(dist)

  topo_order = topological_sort(graph)

  return longest_path(graph,topo_order)
  