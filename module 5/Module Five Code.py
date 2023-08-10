
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:95% !important; }</style>"))


import numpy as np
from IPython.display import Image
from graphviz import Digraph


class SearchNode:
    
    def __init__(self, v):

        self.value = v
        self.inNeighbors = []
        self.outNeighbors = []
        self.status = "unvisited"
        self.color = ""
        
    def hasOutNeighbor(self, v):
        
        return v in self.outNeighbors
        
    def hasInNeighbor(self, v):
        return v in self.inNeighbors
    
    def hasNeighbor(self, v):
        return v in self.inNeighbors or v in self.outNeighbors
    
    def getOutNeighbors(self):
        return self.outNeighbors
    
    def getInNeighbors(self):
        return self.inNeighbors
        
    def addOutNeighbor(self, v):
        self.outNeighbors.append(v)
    
    def addInNeighbor(self, v):
        self.inNeighbors.append(v)
    
    def __str__(self):
        return str(self.value) 


class SearchGraph:
    
    def __init__(self):
        
        self.vertices = []

    def addVertex(self,n):
        
        self.vertices.append(n)
        
    def addDiEdge(self, u, v):
        
        u.addOutNeighbor(v)
        v.addInNeighbor(u)
        
    # add edges in both directions between u and v
    def addBiEdge(self, u, v):
        
        self.addDiEdge(u, v)
        self.addDiEdge(v, u)
        
    # get a list of all the directed edges
    # directed edges are a list of two vertices
    def getDirEdges(self):
        
        ret = []
        for v in self.vertices:
            ret += [ [v, u] for u in v.outNeighbors ]
        return ret
    
    def __str__(self):
        ret = "Graph with:\n" + "\t Vertices:\n\t"
        for v in self.vertices:
            ret += f"{str(v)},"
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b in self.getDirEdges():
            ret += f"({str(a)},{str(b)}) "
        ret += "\n"
        return ret



class SCCNode:
    
    def __init__(self, v):

        self.value = v
        self.inNeighbors = []
        self.outNeighbors = []
        
        self.status = "unvisited"
        self.inTime = None
        self.outTime = None
        
    def hasOutNeighbor(self, v):
        
        return v in self.outNeighbors
        
    def hasInNeighbor(self, v):
        
        return v in self.inNeighbors
    
    def hasNeighbor(self, v):
        return v in self.inNeighbors or v in self.outNeighbors
    
    def getOutNeighbors(self):
        return self.outNeighbors
    
    def getInNeighbors(self):
        return self.inNeighbors
        
    def addOutNeighbor(self, v):
        self.outNeighbors.append(v)
    
    def addInNeighbor(self, v):
        self.inNeighbors.append(v)
    
    def __str__(self):
        return str(self.value) 


class SCCGraph:
    
    def __init__(self):
        
        self.vertices = []

    def addVertex(self,n):
        
        self.vertices.append(n)
        
    # add a directed edge from CS161Node u to CS161Node v
    def addDiEdge(self, u, v):
        
        u.addOutNeighbor(v)
        v.addInNeighbor(u)
        
    # add edges in both directions between u and v
    def addBiEdge(self, u, v):
        
        self.addDiEdge(u, v)
        self.addDiEdge(v, u)
        
    # get a list of all the directed edges
    # directed edges are a list of two vertices
    def getDirEdges(self):
        
        ret = []
        for v in self.vertices:
            ret += [ [v, u] for u in v.outNeighbors ]
        return ret
    
    # reverse the edge between u and v.  Multiple edges are not supported.
    def reverseEdge(self,u,v):
        
        if u.hasOutNeighbor(v) and v.hasInNeighbor(u):
            
            if v.hasOutNeighbor(u) and u.hasInNeighbor(v): 
                return
        
            self.addDiEdge(v, u)
            u.outNeighbors.remove(v)
            v.inNeighbors.remove(u)        
                
    def __str__(self):
        ret = "Graph with:\n" + "\t Vertices:\n\t"
        for v in self.vertices:
            ret += f"{str(v)},"
        ret += "\n"
        ret += "\t Edges:\n\t"
        for a,b in self.getDirEdges():
            ret += f"({str(a)},{str(b)}) "
        ret += "\n"
        return ret


G = SearchGraph()
for i in range(10):
    G.addVertex( SearchNode(i) )

V = G.vertices
for i in range(9):
    G.addDiEdge( V[i], V[i+1] )

print(G)

G = SearchGraph()
for i in ['Melbourne', 'Sydney', 'Brisbane', 'Perth', 'Darwin', 'GoldCoast', 'PortDouglas', 'Cairns']:
    G.addVertex( SearchNode(i) )

V = G.vertices

for i in range(len(V)):
    print(i, V[i].value)

#dot.edge('Melbourne', 'Sydney')
G.addDiEdge( V[0], V[1] )

#dot.edge('Melbourne', 'Brisbane')
G.addDiEdge( V[0], V[2] )

#dot.edge('Sydney', 'Perth')
G.addDiEdge( V[1], V[3] )

#dot.edge('Sydney', 'Cairns')
G.addDiEdge( V[1], V[7] )

#dot.edge('Brisbane', 'Darwin')
G.addDiEdge( V[2], V[4] )

#dot.edge('Brisbane', 'GoldCoast')
G.addDiEdge( V[2], V[5] )

#dot.edge('Darwin', 'Perth')
G.addDiEdge( V[4], V[3] )

#dot.edge('Darwin', 'PortDouglas')
G.addDiEdge( V[4], V[6] )

print(G)


def DFSOne(root):
    
    if root == Null:
        return

    root.visited = True

    for n in root.neighbours:
        if n.visited == False:
            DFS(n)


def DFS_helper(w):
    
    w.status = "inprogress"
    
    for v in w.getOutNeighbors():
        
        if v.status == "unvisited":
            
            DFS_helper(v)
    
    print(w)
    w.status = "done"
    
        
def DFSTwo(w, G):
    
    for v in G.vertices:
        
        v.status = "unvisited"
        
    return DFS_helper(w)


# Let us do the DFS from Melbourne
w = G.vertices[0]

DFSTwo(w, G)


def BFSOne(root):

    visited = [False] * (num_nodes_in_graph)

    # Create a queue for BFS
    queue = [root]

    visited[root] = True

    while queue:

        r = queue.pop(0)
        print(r)

        for n in r.adjacent:

            if visited[n] == False:

                visited[n] = True
                queue.append(n)


def BFSTwo(w, G):
    
    for v in G.vertices:
        v.status = "unvisited"

    n = len(G.vertices)

    Ls = [[] for _ in range(n)]

    Ls[0] = [w]
    w.status = "visited"

    for i in range(n):
        for u in Ls[i]:

            print(u)

            for v in u.getOutNeighbors():

                if v.status == "unvisited":
                    v.status = "visited"
                    Ls[i + 1].append(v)

w = G.vertices[0]

BFSTwo(w, G)


TestG = SearchGraph()
for i in range(4):
    TestG.addVertex( SearchNode(i) )

TestV = TestG.vertices

for i in range(3):
    TestG.addDiEdge( V[i], V[i+1] )

print(TestG)

TestG = SearchGraph()
for i in ['Melbourne', 'Perth', 'Sydney', 'Brisbane']:
    TestG.addVertex( SearchNode(i) )

TestV = TestG.vertices

for i in range(len(TestV)):
    print(i, TestV[i].value)

TestG.addBiEdge( TestV[0], TestV[1] )
TestG.addBiEdge( TestV[1], TestV[2] )
TestG.addBiEdge( TestV[2], TestV[3] )


print(TestG)


def BidirectionalSearch(s, t, G):
    """ Bidirectional search between vertices s and t in graph G.
        Returns a path from s to t if one exists, None otherwise.
        Args:
            s, t: vertices
            G: directed graph
    """
    # Reset all vertices to unvisited
    for v in G.vertices:
        v.status = 'unvisited'

    # Dictionaries to store paths
    path_from_s = {s: [s]}
    path_from_t = {t: [t]}

    # Initialize layers
    Ls1 = [s]
    Ls2 = [t]
    s.status = 'visitedByS'
    t.status = 'visitedByT'

    while Ls1 and Ls2:
        next_layer_s = []
        for u in Ls1:
            for v in u.getOutNeighbors():
                print('Checking edge', u, v)
                if v.status == 'unvisited':
                    v.status = 'visitedByS'
                    path_from_s[v] = path_from_s[u] + [v]
                    print('appending', v)
                    next_layer_s.append(v)
                if v.status == 'visitedByT' and v in path_from_t:
                    print('Found path!')
                    return path_from_s[u] + path_from_t[v][::-1]
                    
        next_layer_t = []
        for u in Ls2:
            print('Checking edge', u, v)
            for v in u.getOutNeighbors():
                if v.status == 'unvisited':
                    v.status = 'visitedByT'
                    path_from_t[v] = path_from_t[u] + [v]
                    print('appending', v)
                    next_layer_t.append(v)
                if v.status == 'visitedByS' and v in path_from_s:
                    print('Found path!')
                    return path_from_s[v] + path_from_t[u][::-1]

        # Swap layers
        Ls1 = next_layer_s
        Ls2 = next_layer_t

    return None
    



BDSearch = BidirectionalSearch(TestG.vertices[0], TestG.vertices[3], TestG)
if BDSearch is None:
    print("No path found")
else:
    for i in BDSearch:
        print(i)


def CheckForBipartite(start_node, graph):
    for node in graph.vertices:
        node.status = 'unvisited'
        node.color = None

    start_node.status = 'visited'
    start_node.color = 'blue'
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        for neighbor in node.getOutNeighbors():
            if neighbor.status == 'unvisited':
                neighbor.status = 'visited'
                neighbor.color = 'red' if node.color == 'blue' else 'blue'
                queue.append(neighbor)
            elif neighbor.color == node.color:
                return False
                
    return True

G = SearchGraph()
for i in range(10):
    G.addVertex( SearchNode(i) )

V = G.vertices
for i in range(9):
    G.addDiEdge( V[i], V[i+1] )

print(G)

G = SearchGraph()
for i in ['Melbourne', 'Sydney', 'Brisbane', 'Perth', 'Darwin', 'GoldCoast', 'PortDouglas', 'Cairns']:
    G.addVertex( SearchNode(i) )

V = G.vertices

for i in range(len(V)):
    print(i, V[i].value)

#dot.edge('Melbourne', 'Sydney')
G.addDiEdge( V[0], V[1] )

#dot.edge('Melbourne', 'Brisbane')
G.addDiEdge( V[0], V[2] )

#dot.edge('Sydney', 'Perth')
G.addDiEdge( V[1], V[3] )

#dot.edge('Sydney', 'Cairns')
G.addDiEdge( V[1], V[7] )

#dot.edge('Brisbane', 'Darwin')
G.addDiEdge( V[2], V[4] )

#dot.edge('Brisbane', 'GoldCoast')
G.addDiEdge( V[2], V[5] )

#dot.edge('Darwin', 'Perth')
G.addDiEdge( V[4], V[3] )

#dot.edge('Darwin', 'PortDouglas')
G.addDiEdge( V[4], V[6] )

print(G)

print("Graph is Bipartite: " + str(CheckForBipartite(w, G)))


a = SCCNode("A")
b = SCCNode("B")
c = SCCNode("C")
d = SCCNode("D")
e = SCCNode("E")
f = SCCNode("F")

G = SCCGraph()
V = [a, b, c, d, e, f]
for v in V:
    G.addVertex(v)

# Edges forming three SCCs
# SCC 1: A and B
# SCC 2: C, D and E
# SCC 3: F (single vertex SCC), with an edge connecting to A
E = [(a, b), (b, a),
     (c, d), (d, e), (e, c),
     (d, c), (e, d),
     (f, a)] # Edge connecting F to A
for x, y in E:
    G.addDiEdge(x, y)

print(G)

def SCC(G):
    def DFS_helper(v, time, component):
        v.status = 'inprogress'
        component.append(v) # add the vertex to the current component
        v.inTime = time
        time += 1
        for w in v.getOutNeighbors():
            if w.status == 'unvisited':
                time = DFS_helper(w, time, component)
        v.status = 'done'
        v.outTime = time
        time += 1
        return time

    time = 1
    for v in G.vertices:
        v.status = 'unvisited'
    for v in G.vertices:
        if v.status == 'unvisited':
            time = DFS_helper(v, time, []) # Update the time here

    for v in G.vertices:
        for w in v.getOutNeighbors():
            G.reverseEdge(v, w)


    SCCs = []
    stack = sorted(G.vertices, key=lambda x: x.outTime, reverse=True)
    for v in stack:
        v.status = 'unvisited'
    time = 1
    for v in stack:
        if v.status == 'unvisited':
            component = []
            time = DFS_helper(v, time, component) # Update the time here
            SCCs.append(component)

    return SCCs


SCCs = SCC(G)
for scc in SCCs:
    print([str(v) for v in scc])



