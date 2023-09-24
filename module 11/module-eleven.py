# %% [markdown]
# # SIT320 Advanced Algorithms
# ## Module 11 - Network Based Algorithms

# %% [markdown]
# ### Task 1 Karger's Algorithm

# %%
import copy
import random
import time
import math

# %%
class Node:
    
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.weights = []
    
    def getNeighbours(self):
        return self.neighbors

    def getWeights(self):
        return self.weights

    def __str__(self):
        return str(self.data)

class Graph:

    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
    
    def add_edge(self, node1, node2, weight):
        if node1 in self.nodes and node2 in self.nodes:
            node1.neighbors.append(node2)
            node1.weights.append(weight)
            node2.neighbors.append(node1)
            node2.weights.append(weight)

    def getNeighbours(self):
        ret = []
        for v in self.nodes:
            ret.extend((v, (n, w)) for n, w in zip(v.getNeighbours(), v.getWeights()))
        return ret
        
    def __str__(self):
        ret = "Graph with:\n" + "\t Vertices:\n\t"
        for v in self.nodes:
            ret += f"{str(v)},"
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a, b in self.getNeighbours():
            ret += f"({str(a)}->{str(b[0])} , {str(b[1])})) "
        ret += "\n"
        return ret

# %%
def Kargers(G):
    while len(G.nodes) > 2:
        edges = G.getNeighbours()
        # get weights
        weights = [e[1][1] for e in edges]
        # get probabilities
        probs = [w/sum(weights) for w in weights]
        # find the index of the edge with max probability
        e = edges[probs.index(max(probs))]
        # print(f"Contracting edge {e[0]}->{e[1][0]} with weight {e[1][1]}")
        # contract edge
        G.add_edge(e[0], e[1][0], e[1][1])  
        # remove self-loops if any
        if e[0] in e[1][0].getNeighbours():
            e[1][0].getNeighbours().remove(e[0])
        # remove edge
        G.nodes.remove(e[0])
        # print graph
        # print(G)
    # return min-cut
    return len(G.nodes[0].getNeighbours())
    


# %%
# keep total time
def runKargers(G):    
    return Kargers(G)

answer = []
globalTime = 0
print("Running Karger's algorithm 438 times")
bestCut = math.inf
start = time.time()
for i in range(438):
    G = Graph()
    for i in range(20):
        G.add_node(Node(i))
    G.add_edge(G.nodes[0], G.nodes[1], random.randint(1, 10))
    G.add_edge(G.nodes[0], G.nodes[2], random.randint(1, 10))
    G.add_edge(G.nodes[1], G.nodes[2], random.randint(1, 10))
    G.add_edge(G.nodes[1], G.nodes[3], random.randint(1, 10))
    G.add_edge(G.nodes[2], G.nodes[3], random.randint(1, 10))
    G.add_edge(G.nodes[2], G.nodes[4], random.randint(1, 10))
    G.add_edge(G.nodes[3], G.nodes[4], random.randint(1, 10))
    G.add_edge(G.nodes[3], G.nodes[5], random.randint(1, 10))
    G.add_edge(G.nodes[4], G.nodes[5], random.randint(1, 10))
    G.add_edge(G.nodes[4], G.nodes[6], random.randint(1, 10))
    G.add_edge(G.nodes[5], G.nodes[6], random.randint(1, 10))
    G.add_edge(G.nodes[5], G.nodes[7], random.randint(1, 10))
    G.add_edge(G.nodes[6], G.nodes[7], random.randint(1, 10))
    G.add_edge(G.nodes[6], G.nodes[8], random.randint(1, 10))
    G.add_edge(G.nodes[7], G.nodes[8], random.randint(1, 10))
    G.add_edge(G.nodes[7], G.nodes[9], random.randint(1, 10))
    G.add_edge(G.nodes[8], G.nodes[9], random.randint(1, 10))
    G.add_edge(G.nodes[8], G.nodes[10], random.randint(1, 10))
    G.add_edge(G.nodes[9], G.nodes[10], random.randint(1, 10))
    G.add_edge(G.nodes[9], G.nodes[11], random.randint(1, 10))
    G.add_edge(G.nodes[10], G.nodes[11], random.randint(1, 10))
    G.add_edge(G.nodes[10], G.nodes[12], random.randint(1, 10))
    G.add_edge(G.nodes[11], G.nodes[12], random.randint(1, 10))
    G.add_edge(G.nodes[11], G.nodes[13], random.randint(1, 10))
    G.add_edge(G.nodes[12], G.nodes[13], random.randint(1, 10))
    G.add_edge(G.nodes[12], G.nodes[14], random.randint(1, 10))
    G.add_edge(G.nodes[13], G.nodes[14], random.randint(1, 10))
    G.add_edge(G.nodes[13], G.nodes[15], random.randint(1, 10))
    G.add_edge(G.nodes[14], G.nodes[15], random.randint(1, 10))
    G.add_edge(G.nodes[14], G.nodes[16], random.randint(1, 10))
    G.add_edge(G.nodes[15], G.nodes[16], random.randint(1, 10))
    G.add_edge(G.nodes[15], G.nodes[17], random.randint(1, 10))
    G.add_edge(G.nodes[16], G.nodes[17], random.randint(1, 10))
    G.add_edge(G.nodes[16], G.nodes[18], random.randint(1, 10))
    G.add_edge(G.nodes[17], G.nodes[18], random.randint(1, 10))
    G.add_edge(G.nodes[17], G.nodes[19], random.randint(1, 10))
    G.add_edge(G.nodes[18], G.nodes[19], random.randint(1, 10))
    G.add_edge(G.nodes[18], G.nodes[0], random.randint(1, 10))
    G.add_edge(G.nodes[19], G.nodes[0], random.randint(1, 10))

    candidateCut = min(bestCut, runKargers(copy.deepcopy(G)))
    if candidateCut < bestCut:
        bestCut = candidateCut
    end = time.time()
    globalTime += end - start
    start = end
print(f"Time Taken: {globalTime}")
print(f"Best cut: {bestCut}")

# %%

def KargersRandom(G):
    while len(G) > 2:
        # pick random edge
        v1 = random.choice(list(G.keys()))
        v2 = random.choice(G[v1])
        # merge v2 into v1
        G[v1].extend(G[v2])
        # print the edge that is being contracted
        # print(f"Contracting edge {v1}->{v2}")
        # replace all v2 with v1
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        # remove self-loops
        while v1 in G[v1]:
            G[v1].remove(v1)
        # remove v2
        del G[v2]
    # return min-cut
    return len(list(G.values())[0])

G = {i: [] for i in range(20)}
G[0].extend([1, 2, 3, 4, 5])
G[1].extend([0, 2, 3, 4, 5])
G[2].extend([0, 1, 3, 4, 5, 6])
G[3].extend([0, 1, 2, 4, 5, 6, 7])
G[4].extend([0, 1, 2, 3, 5, 6, 7, 8, 9])
G[5].extend([0, 1, 2, 3, 4, 6, 7, 8, 9, 10])
G[6].extend([2, 3, 4, 5, 7, 8, 9, 10, 11])
G[7].extend([3, 4, 5, 6, 8, 9, 10, 11, 12])
G[8].extend([4, 5, 6, 7, 9, 10, 11, 12, 13])
G[9].extend([4, 5, 6, 7, 8, 10, 11, 12, 13, 14])
G[10].extend([5, 6, 7, 8, 9, 11, 12, 13, 14, 15])
G[11].extend([6, 7, 8, 9, 10, 12, 13, 14, 15, 16])
G[12].extend([7, 8, 9, 10, 11, 13, 14, 15, 16, 17])
G[13].extend([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
G[14].extend([9, 10, 11, 12, 13, 15, 16, 17, 18, 19])
G[15].extend([10, 11, 12, 13, 14, 16, 17, 18, 19])
G[16].extend([11, 12, 13, 14, 15, 17, 18, 19])
G[17].extend([12, 13, 14, 15, 16, 18, 19])
G[18].extend([13, 14, 15, 16, 17, 19])
G[19].extend([14, 15, 16, 17, 18])


def test_karger(graph, n):
    # compute the number of times to run Karger's algorithm
    num_runs = int(math.ceil(n * (n - 1) / 2 * math.log(1 / 0.1)))
    print(f"Running Karger's algorithm {num_runs} times")
    bestCut = float('inf')
    start = time.time()
    for _ in range(num_runs):
        # make a copy of the graph
        graph_copy = copy.deepcopy(graph)
        # run Karger's algorithm on the copied graph
        candidateCut = KargersRandom(graph_copy)
        # update the best min cut
        if candidateCut < bestCut:
            bestCut = candidateCut
    end = time.time()
    print(f"Time taken: {end-start} seconds")
    print(f"Best min-cut: {bestCut}")
        

test_karger(G, 20)


# %%

# define the nodes and edges
G = {i: [] for i in range(20)}
G[0].extend([1, 2, 3, 4, 5])
G[1].extend([0, 2, 3, 4, 5])
G[2].extend([0, 1, 3, 4, 5, 6])
G[3].extend([0, 1, 2, 4, 5, 6, 7])
G[4].extend([0, 1, 2, 3, 5, 6, 7, 8, 9])
G[5].extend([0, 1, 2, 3, 4, 6, 7, 8, 9, 10])
G[6].extend([2, 3, 4, 5, 7, 8, 9, 10, 11])
G[7].extend([3, 4, 5, 6, 8, 9, 10, 11, 12])
G[8].extend([4, 5, 6, 7, 9, 10, 11, 12, 13])
G[9].extend([4, 5, 6, 7, 8, 10, 11, 12, 13, 14])
G[10].extend([5, 6, 7, 8, 9, 11, 12, 13, 14, 15])
G[11].extend([6, 7, 8, 9, 10, 12, 13, 14, 15, 16])
G[12].extend([7, 8, 9, 10, 11, 13, 14, 15, 16, 17])
G[13].extend([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
G[14].extend([9, 10, 11, 12, 13, 15, 16, 17, 18, 19])
G[15].extend([10, 11, 12, 13, 14, 16, 17, 18, 19])
G[16].extend([11, 12, 13, 14, 15, 17, 18, 19])
G[17].extend([12, 13, 14, 15, 16, 18, 19])
G[18].extend([13, 14, 15, 16, 17, 19])
G[19].extend([14, 15, 16, 17, 18])


def EdgeContraction(G):
    length = len(G.keys())//2
    # print(f"Length: {length}")
    while len(G) > length:
        # pick random edge
        v1 = random.choice(list(G.keys()))
        v2 = random.choice(G[v1])
        # merge v2 into v1
        G[v1].extend(G[v2])
        # print the edge that is being contracted
        # print(f"Contracting edge {v1}->{v2}")
        # replace all v2 with v1
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        # remove self-loops
        while v1 in G[v1]:
            G[v1].remove(v1)
        # remove v2
        del G[v2]
    # return G
    return G


def Kargers4(G):
    if len(G) == 2:
        return len(G[list(G.keys())[0]])
    G1 = EdgeContraction(copy.deepcopy(G))
    # print(f"G1: {G1}")
    G2 = EdgeContraction(copy.deepcopy(G))
    # print(f"G2: {G2}")
    G3 = EdgeContraction(copy.deepcopy(G))
    # # print(f"G3: {G3}")
    G4 = EdgeContraction(copy.deepcopy(G))
    # print(f"G4: {G4}")
    return min(Kargers4(G1), Kargers4(G2), Kargers4(G3), Kargers4(G4))
    

start = time.time()
bestCut = Kargers4(G)
end = time.time()
print("Running Kargers4 one time")
print(f"Time taken: {end-start} seconds")
print(f"Best cut: {bestCut}")

# %% [markdown]
# ### Task 2 Ford-Fulkerson Algorithm

# %%
class Graph():
    def __init__(self):
        self.edges = {}
        self.weights = {}
        self.flow = {}

    def add_node(self, node):
        self.edges[node] = []
        self.flow[node] = {}
    
    def add_di_edge(self, from_node, to_node, weight, flow=0):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight
        self.flow[from_node][to_node] = flow
        self.flow[to_node][from_node] = 0
        
    def add_bi_edge(self, node1, node2, weight):
        self.add_di_edge(node1, node2, weight)
        self.add_di_edge(node2, node1, weight)

    def update_flow(self, path, flow):
        print(f"Updating flow on path {path} with flow {flow}")
        for i in range(len(path)-1):
            edge = (path[i], path[i+1])
            self.flow[path[i]][path[i+1]] += flow
            self.flow[path[i+1]][path[i]] -= flow

            

    def get_path(self, start, end, path):
        if start not in self.edges:
            return None
        path = path + [start]
        if start == end:
            return path
        for node in self.edges[start]:
            if node not in path:
                if newpath := self.get_path(node, end, path):
                    return newpath
        return None
    
class Node():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

T = Graph()
T.add_node("s")
T.add_node("a")
T.add_node("b")
T.add_node("c")
T.add_node("d")
T.add_node("e")
T.add_node("f")
T.add_node("t")
T.add_di_edge("s", "a", 4, 0)
T.add_di_edge("s", "b", 2, 0)
T.add_di_edge("s", "c", 6, 0)
T.add_di_edge("a", "d", 3, 0)
T.add_di_edge("a", "e", 6, 0)
T.add_di_edge("b", "e", 3, 0)
T.add_di_edge("c", "f", 10, 0)
T.add_di_edge("d", "t", 4, 0)
T.add_di_edge("e", "t", 4, 0)
T.add_di_edge("f", "b", 3, 0)
T.add_di_edge("f", "t", 4, 0)

# print(f"T.edges: {T.edges}")
# print(f"T.weights: {T.weights}")
# print(f"T.flow: {T.flow}")


class ResidualGraph(Graph):
    def __init__(self, graph):
        super().__init__()
        for node in graph.edges:
            self.add_node(node)
            for neighbor in graph.edges[node]:
                if neighbor not in self.edges:
                    self.add_node(neighbor)
                self.add_bi_edge(node, neighbor, graph.weights[(node, neighbor)])
        self.flow = copy.deepcopy(graph.flow)
    
    def update_weights(self):
        for node in self.edges:
            for neighbor in self.edges[node]:
                forward_edge = (node, neighbor)
                backward_edge = (neighbor, node)
                residual_capacity = self.weights[forward_edge] - self.flow[node][neighbor]
                self.weights[forward_edge] = residual_capacity
                self.weights[backward_edge] = self.flow[node][neighbor]


# print(f"residual_graph.edges: {residual_graph.edges}")
# print(f"residual_graph.weights: {residual_graph.weights}")

def is_reachable(residual_graph, s, t):
    visited = set()
    stack = [s]
    while stack:
        node = stack.pop()
        if node == t:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in residual_graph.edges[node]:
                if residual_graph.weights[(node, neighbor)] > 0:
                    stack.append(neighbor)
    return False

# print(f"Is t reachable from s? {is_reachable(residual_graph, 's', 't')}")

def get_path(G, residual_graph, s, t, path=None):
    if path is None:
        path = []
    if s == t:
        return path
    for neighbor in G.edges[s]:
        if G.flow[s][neighbor] < G.weights[(s, neighbor)] and neighbor not in path:
            newpath = get_path(G, residual_graph, neighbor, t, path + [neighbor])
            if newpath is not None:
                return newpath
    return None

def incerease_flow(G, residual_graph, s, t):
    path = get_path(G, residual_graph, s, t)
    print(f"path: {path}")
    flow = min(residual_graph.weights[(path[i], path[i+1])] for i in range(len(path)-1))
    G.update_flow(path, flow)
    print(f"G.flow: {G.flow}")
    residual_graph.update_weights(G)
    return flow

def Ford_Fulkerson(G, residual_graph, s, t):
    max_flow = 0
    while is_reachable(residual_graph, s, t):
        path = get_path(G, residual_graph, s, t)
        if path is None:
            break
        flow = min(residual_graph.weights[(path[i], path[i+1])] for i in range(len(path)-1))
        G.update_flow(path, flow)
        residual_graph.update_weights()
        max_flow += flow
    return max_flow
    
    

def print_min_cut(G, residual_graph, s, t):
    # Run Ford-Fulkerson algorithm to compute maximum flow
    max_flow = Ford_Fulkerson(G, residual_graph, s, t)
    # now we need to print the min-cut
    # we need to find all vertices reachable from s in the residual graph
    visited = set()
    stack = [s]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in residual_graph.edges[node]:
                if residual_graph.weights[(node, neighbor)] > 0:
                    stack.append(neighbor)
    # print(f"Vertices reachable from s: {visited}")
    # now we need to print all edges between visited and not visited
    min_cut = 0
    for node in visited:
        for neighbor in residual_graph.edges[node]:
            if neighbor not in visited and residual_graph.weights[(node, neighbor)] > 0:
                queue.append(neighbor)
    
    # Identify the edges that form the minimum cut
    min_cut = set()
    for node in visited:
        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                # keep track of edge weights in the cut
                min_cut += residual_graph.weights[(neighbor, node)]
                print(f"Min-cut edge: {node}->{neighbor}")
    
    print(f"Max flow value: {max_flow}")
    print(f"Min-cut value: {min_cut}")

    

print(f"Max flow: {Ford_Fulkerson(T, ResidualGraph(T), 's', 't')}")
print(f"Min cut: {max_flow_min_cut(T, 's', 't')}")


