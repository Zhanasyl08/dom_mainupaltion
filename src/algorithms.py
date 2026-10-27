import heapq


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.components -= 1
        return True


def dsu(n, operations):
    uf = DSU(n)
    answer = []
    largest = 1 if n else 0
    for u, v in operations:
        uf.union(u, v)
        largest = max(largest, uf.size[uf.find(u)])
        answer.append([uf.components, largest])
    return answer


def kruskal(n, edges):
    uf = DSU(n)
    chosen = []
    total = 0
    for idx, (u, v, w) in sorted(enumerate(edges), key=lambda x: (x[1][2], x[0])):
        if uf.union(u, v):
            chosen.append(idx)
            total += w
    return {"cost": total, "edge_ids": chosen, "components": uf.components}


def prim(n, edges):
    adj = [[] for _ in range(n)]
    for idx, (u, v, w) in enumerate(edges):
        adj[u].append((w, idx, v))
        adj[v].append((w, idx, u))
    seen = [False] * n
    total = 0
    chosen = []
    components = 0
    for start in range(n):
        if seen[start]:
            continue
        components += 1
        seen[start] = True
        heap = list(adj[start])
        heapq.heapify(heap)
        while heap:
            weight, idx, v = heapq.heappop(heap)
            if seen[v]:
                continue
            seen[v] = True
            chosen.append(idx)
            total += weight
            for item in adj[v]:
                if not seen[item[2]]:
                    heapq.heappush(heap, item)
    return {"cost": total, "edge_ids": chosen, "components": components}


def scc(n, edges):
    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        rev[v].append(u)
    visited = [False] * n
    order = []
    for start in range(n):
        if visited[start]:
            continue
        visited[start] = True
        stack = [(start, 0)]
        while stack:
            u, i = stack[-1]
            if i == len(adj[u]):
                order.append(u)
                stack.pop()
            else:
                v = adj[u][i]
                stack[-1] = (u, i + 1)
                if not visited[v]:
                    visited[v] = True
                    stack.append((v, 0))
    labels = [-1] * n
    count = 0
    for start in reversed(order):
        if labels[start] != -1:
            continue
        labels[start] = count
        stack = [start]
        while stack:
            u = stack.pop()
            for v in rev[u]:
                if labels[v] == -1:
                    labels[v] = count
                    stack.append(v)
        count += 1
    condensation = sorted({(labels[u], labels[v]) for u, v in edges if labels[u] != labels[v]})
    return {"components": count, "labels": labels, "condensation": [list(p) for p in condensation]}


def topo(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    state = [0] * n
    order = []
    for start in range(n):
        if state[start]:
            continue
        state[start] = 1
        stack = [(start, 0)]
        while stack:
            u, i = stack[-1]
            if i == len(adj[u]):
                state[u] = 2
                order.append(u)
                stack.pop()
                continue
            v = adj[u][i]
            stack[-1] = (u, i + 1)
            if state[v] == 1:
                return {"acyclic": False, "order": []}
            if state[v] == 0:
                state[v] = 1
                stack.append((v, 0))
    order.reverse()
    return {"acyclic": True, "order": order}


def dag(n, edges, source):
    result = topo(n, [(u, v) for u, v, _ in edges])
    if not result["acyclic"]:
        return {"acyclic": False, "distance": [], "parent_edge": []}
    adj = [[] for _ in range(n)]
    for idx, (u, v, w) in enumerate(edges):
        adj[u].append((v, w, idx))
    distance = [None] * n
    parent_edge = [-1] * n
    distance[source] = 0
    for u in result["order"]:
        if distance[u] is None:
            continue
        for v, w, idx in adj[u]:
            new_dist = distance[u] + w
            if distance[v] is None or new_dist < distance[v]:
                distance[v] = new_dist
                parent_edge[v] = idx
    return {"acyclic": True, "distance": distance, "parent_edge": parent_edge}


def reconstruct_route(target, parent_edge, edges, source):
    if target == source:
        return [source]
    path = [target]
    current = target
    for _ in range(len(parent_edge)):
        idx = parent_edge[current]
        if idx == -1:
            return []
        current = edges[idx][0]
        path.append(current)
        if current == source:
            return path[::-1]
    return []
