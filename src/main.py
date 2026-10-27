import json
import sys
from algorithms import dsu, kruskal, prim, scc, topo, dag


def solve(request):
    method = request["method"].lower()
    n = request["n"]
    edges = request.get("edges", [])
    if method == "dsu":
        return {"result": dsu(n, request["operations"])}
    if method == "kruskal":
        return kruskal(n, edges)
    if method == "prim":
        return prim(n, edges)
    if method == "scc":
        return scc(n, edges)
    if method == "topo":
        return topo(n, edges)
    if method == "dag":
        return dag(n, edges, request["source"])
    raise ValueError("Unknown method")


def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            result = solve(json.loads(line))
            print(json.dumps(result, separators=(",", ":")))
        except (ValueError, KeyError, TypeError, IndexError) as error:
            print(json.dumps({"error": str(error)}))


if __name__ == "__main__":
    main()
