## Strategy
### top-down perspective
1. understand the problem
- the game is a draw if all the squares are filled and there is no winner.
- the game is played on a 3x3 grid.
- the game is played by two players, one player is X and the other is O.
- the players take turns to place their symbol on the grid.
- the game ends when there is a winner or a draw.
- tic tac toe is futile game. there is no winning strategy for either player if both players play optimally. 
- tic tac toe is a zero sum game. if one player wins, the other player loses. if there is a draw, both players have the same score.
- it is a game of perfect information. previous moves are known to both players at the time of making a decision.  
- there are 8 winning combinations. 3 horizontal, 3 vertical and 2 diagonal.
- trying all possible moves is not feasible(brute force).
    - **there are 255,168 possible games.**
    - **it's not exciting as a thought experiment.**

2. plan a solution - **GRAPH SEARCH**
- search all possible moves and choose the optimal move. 
    - **if there is a winning move take it, otherwise take a move that does not allow the opponent to win.**
    - **take the centre square if it is available.**
    - **take a corner square if it is available.**
    - **take an edge square if it is available.**
- use a heuristic to choose the optimal move.
- using a game tree.
    - **the game tree is a directed graph.**
    - **the nodes are the states of the game.**
    - **the edges are the moves.**
    - **the root node is the initial state of the game.**
    - **the leaf nodes are the terminal states of the game.**
    - **sreach part of the tree, and then evaluate the leaf nodes.**

3. solve


4. test

---

### some term definitions
#### branching factor - the number of child nodes a node has.
#### depth - the number of edges from the root node to a node.
#### ply - a move by one player.
#### minimax - a decision rule for minimizing the possible loss for a worst case scenario.
#### heuristic - a function that ranks alternatives in search algorithms at each branching step based on available information to decide which branch to follow.

---

### minimax algorithm

def max-value(state,depth):
    if (depth == 0): return value(state)
    v = -infinite
    for each s in SUCCESSORS(state):
        v = MAX(v,min-value(s,depth-1))
    return v

def min-value(state,depth):
    if (depth == 0): return value(state)
        v = infinite
    for each s in SUCCESSORS(state):
        v = MIN(v,max-value(s,depth-1))
    return v

---

### alpha-beta pruning

a = best score for max-player (helen)
b = best score for min-player (stavros)
initially, we call max-value(initial, -infinite, infinite, max-depth)

def max-value(state, a, b, depth):
    if (depth == 0): return value(state)
    for s in SUCCESSORS(state):
        a = max(a, min-value(s,a,b,depth-1))
        if a >= b: return a \\ this ia a cutoff point
    return a

def min-value(state, a, b, depth):
    if (depth == 0): return value(state)
    for s in SUCCESSORS(state):
        b = min(b,max-value(s,a,b,depth-1))
        if b <= a: return b \\ this is a cutoff point
    return b

---

#### Pseuo-code