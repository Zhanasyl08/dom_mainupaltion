# Assignment 3 — Graph Algorithms

**Student:** Zhanassyl Omar  
**Group:** SE-2538  
**Course:** Design and Analysis of Algorithms

## Implemented algorithms

1. `dsu` — path compression and union by size, returns components and current largest component after every union.
2. `kruskal` — minimum spanning forest using sorted edges and DSU.
3. `prim` — minimum spanning forest using a priority queue; starts again for each separate component.
4. `scc` — Kosaraju's algorithm with iterative DFS, plus condensation graph.
5. `topo` — iterative three-state DFS and directed cycle detection.
6. `dag` — checks acyclicity, then shortest paths in topological order (negative weights supported).

## Project files

- `src/algorithms.py` — graph algorithms
- `src/main.py` — UTF-8 JSON Lines input/output
- `submission.json` — Python entry point
- `tests/test_algorithms.py` — unit tests
- `tools/run.py` — setup/test script
- `tools/benchmark.py` — benchmarking program
- `ANALYSIS.md` — explanation and complexity analysis

## Run

Python 3.12 or later is recommended. No external packages are required.

```bash
python tools/run.py --setup
python tools/run.py --check
python src/main.py < examples.jsonl
python tools/benchmark.py
```

Each input line is a JSON request, and each output line is one JSON result. State is reset for every request.

## Request structure used in this project

- Common fields: `method`, `n`, `edges`.
- `dsu`: `operations` contains pairs `[u,v]`.
- `kruskal`, `prim`, `dag`: `edges` contains `[u,v,w]`.
- `scc`, `topo`: `edges` contains `[u,v]`.
- `dag`: `source` is the start vertex.
- Vertex IDs are from `0` to `n-1`. Edge IDs are their original input positions.

Example input:

```json
{"method":"kruskal","n":3,"edges":[[0,1,4],[1,2,2],[0,2,10]]}
```

Example output:

```json
{"cost":6,"edge_ids":[1,0],"components":1}
```

`dag` uses `null` for unreachable distances, `-1` for an absent parent edge, and `0` for source distance.

**Note:** The assignment screenshot references a separate official template and full JSON specification, but those files were not provided. These keys and `submission.json` fields are a working interface, not a confirmed match to the official public checker. The official template is needed to match its exact contract.

## Summary

I implemented six graph algorithms using Python lists, sets, a heap, and DSU. I tested disconnected graphs, cycles, negative weights, parallel edges, self-loops, empty graphs, and deep graphs. I used iterative DFS to avoid recursion errors on large inputs.
