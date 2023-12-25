import regex

file = open("input.txt", "r").read()
lines = file.split("\n")

G = {}
V = {}
n = 0

for line in lines:
    edges = regex.findall("\w{3}", line)
    
    for edge in edges:
        if not edge in V:
            V[edge] = n
            n += 1
    
    G[V[edges[0]]] = [V[v] for v in edges[1:]]

def pathfinderDFS(graph, s, t, prev, returnVisited):
    S = [s]
    visited = set()
    
    while len(S) > 0:
        v = S.pop()
        visited.add(v)
        
        if v == t:
            return True
    
        for u, value in enumerate(graph[v]):
            if not u in visited and value > 0:
                S.append(u)
                visited.add(u)
                prev[u] = v
    
    if returnVisited:
        return visited
    else:
        return False

def ford_fulkerson(G, n, s, t):
    resiudal = [[0] * n for i in range(n)]
    
    for v in G:
        for u in G[v]:
            resiudal[v][u] = 1
            resiudal[u][v] = 1
    
    prev = [-1] * len(resiudal)
    maxFlow = 0
    
    while pathfinderDFS(resiudal, s, t, prev, False):
        pathFlow = n
        
        v = t
        while(v != s):
            pathFlow = min(pathFlow, resiudal[prev[v]][v])
            v = prev[v]
        
        v = t
        while(v != s):
            u = prev[v]
            resiudal[u][v] -= pathFlow
            resiudal[v][u] += pathFlow
            v = prev[v]
        
        maxFlow += pathFlow
    
    return (maxFlow, resiudal)

for s in range(n):
    for t in range(s):
        minCut, resiudal = ford_fulkerson(G, n, s, t)
        
        if minCut == 3:
            count = len(pathfinderDFS(resiudal, s, t, [-1] * len(resiudal), True))
            print(count * (n - count))
            exit()