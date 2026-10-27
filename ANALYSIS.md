# Assignment 3 — Analysis

**Name:** Zhanassyl Omar  
**Group:** SE-2538

## 1. Implementation steps

I used Python for all algorithms. First, I implemented DSU with path compression and union by size. Next, I implemented Kruskal and Prim for minimum spanning forests. After that, I added Kosaraju, topological sorting, and shortest paths in DAGs. I used iterative DFS for large graphs. Finally, I wrote unit tests and ran timing measurements.

## 2. Algorithms and complexity

| Method | Time | Additional memory | Explanation |
|---|---|---|---|
| DSU | O((n+q) α(n)) | O(n+q) including returned answers | Almost constant time unions and finds |
| Kruskal | O(m log m + m α(n)) | O(n+m) | Sort edges, then add only edges between separate sets |
| Prim | O((n+m) log(m+1)) | O(n+m) | Priority queue and restart for separate components |
| SCC | O(n+m) | O(n+m) | Two DFS passes using forward and reverse graphs |
| Topological sort | O(n+m) | O(n+m) | Three colors for cycle detection |
| DAG shortest paths | O(n+m) | O(n+m) | Topological sort, then relax each edge once |

Here `n` is the vertex count, `m` is the edge count, `q` is the number of union operations, and `α(n)` is the inverse Ackermann function.

## 3. Correctness and special cases

- **DSU:** Every union connects two previously separate components or keeps the graph unchanged. Its largest component value never decreases.
- **Kruskal:** It considers edges by increasing weight and accepts an edge only if it connects two different components. By the cut property, the accepted edges form a minimum spanning forest.
- **Prim:** It adds the minimum available edge crossing from the visited vertices to a new vertex. Starting again from each unvisited vertex handles disconnected graphs.
- **SCC:** The second Kosaraju pass on the reversed graph assigns each strongly connected component exactly one label. Condensation edges exclude intra-component links and duplicates.
- **Topological sort:** A directed edge to a gray vertex means a cycle. Otherwise, the reverse of DFS finishing order is a valid topological ordering.
- **DAG:** Processing vertices in topological order guarantees all predecessors have already been considered. Thus, each relaxation gives the minimum source distance, even for negative edge weights.

Tests cover disconnected graphs, empty graphs, self-loops, parallel edges, negative weights, unreachable targets, directed cycles, and deep graphs (30,000 vertices). The `reconstruct_route()` helper returns the source-to-target vertex path using original edge IDs and returns an empty list when the target is unreachable. It also handles the source itself.

State is created separately for every JSON input line. Unreachable DAG distances are `null`, unreachable parent edges are `-1`, and the source has distance `0` and parent `-1`.

## 4. Tests and benchmarking

Run tests:

```bash
python tools/run.py --check
```

Run benchmark:

```bash
python tools/benchmark.py
```

Benchmarks use random graphs with seed 2538 and graph sizes 1,000, 5,000, and 10,000. Each run measures one call using `time.perf_counter()`. Input generation, imports, and printing are outside the measured interval. Warm-up, repeated median timings, and machine-independent reproducibility are not provided; these numbers are illustrative, not comparable across computers. The recorded results are in `benchmark_results.csv`.

| n | m | DSU (s) | Kruskal (s) | Prim (s) | SCC (s) | Topo (s) | DAG (s) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1,000 | 3,000 | 0.004093 | 0.062765 | 0.002835 | 0.001514 | 0.000197 | 0.001338 |
| 5,000 | 15,000 | 0.012260 | 0.015570 | 0.026849 | 0.007322 | 0.000893 | 0.010036 |
| 10,000 | 30,000 | 0.110492 | 0.042653 | 0.065360 | 0.022797 | 0.002409 | 0.025691 |

In this benchmark the topological sort receives a general directed graph and may find a cycle early, so those timings do not measure a full traversal in every case. The DAG benchmark builds acyclic edges separately. The results are affected by the Python runtime and machine load.

## 5. Conclusion

I learned how DSU supports minimum spanning forests, how DFS can detect strongly connected components and directed cycles, and why shortest paths in a DAG can be computed using topological order. Iterative DFS also helped to handle deep graphs without recursion limits.
