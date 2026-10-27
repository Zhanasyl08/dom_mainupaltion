import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from algorithms import dsu, kruskal, prim, scc, topo, dag

random.seed(2538)
print('method,n,m,seconds')
for n in (1000, 5000, 10000):
    m = 3 * n
    undirected = [[random.randrange(n), random.randrange(n), random.randrange(-100, 101)] for _ in range(m)]
    directed = [[random.randrange(n), random.randrange(n)] for _ in range(m)]
    acyclic = [[min(u, v), max(u, v), w] for u, v, w in undirected if u != v]
    tasks = [
        ('dsu', lambda: dsu(n, [[u, v] for u, v, _ in undirected])),
        ('kruskal', lambda: kruskal(n, undirected)),
        ('prim', lambda: prim(n, undirected)),
        ('scc', lambda: scc(n, directed)),
        ('topo', lambda: topo(n, directed)),
        ('dag', lambda: dag(n, acyclic, 0)),
    ]
    for name, function in tasks:
        start = time.perf_counter()
        function()
        elapsed = time.perf_counter() - start
        print(f'{name},{n},{m},{elapsed:.6f}')
