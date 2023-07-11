## Strategy
### top-down perspective
1. understand the problem
- the game is played on a 3x3 grid.
- the game is played by two players, one player is X and the other is O.
- the players take turns to place their symbol on the grid.
- the game ends when there is a winner or a draw.
- the game is a draw if all the squares are filled and there is no winner.
- tic tac toe is a futile game. 
    - **there is no winning strategy for either player if both players play optimally.** 
- tic tac toe is a zero sum game. 
    - **if one player wins, the other player loses. if there is a draw, both players have the same score.**
- it is a game of perfect information. 
    - **previous moves are known to both players at the time of making a decision.**  
- there are 8 winning combinations. 
    - **3 horizontal, 3 vertical and 2 diagonal.**
- brute force is feasible.
    - **there are 255,168 possible games.**
    - **there are better ways to solve the game.**
- depth first search is more interesting a faster way to solve the game 
- space complexity is O(b^m) where b is the branching factor and m is the maximum depth of the game tree.

2. plan a solution - **GRAPH SEARCH**
- search all possible moves and choose the optimal move. 
- use a heuristic to choose the optimal move.
    - **if there is a winning move take it, otherwise take a move that does not allow the opponent to win.**
- using a game tree.
    - **the game tree is a directed graph.**
    - **the root node is the initial state of the game.**
    - **the nodes are the states of the game.**
    - **the edges are the moves.**
    - **the leaf nodes are the terminal states of the game.**

3. solve


4. test

---

### some term definitions
#### branching factor - the number of child nodes a node has.
#### depth - the number of edges from the root node to a node.
#### ply - a move by one player.
#### minimax - a decision rule for minimizing the possible loss for a worst case scenario.
#### heuristic - a function that ranks alternatives in search algorithms at each branching step based on available information to decide which branch to follow.
#### zer0-sum game - a game in which the sum of the payoffs to all players is zero, so that one player gains at the expense of another.
#### depth limit - the maximum depth of the game tree that is searched.
#### game thoery - the study of mathematical models of strategic interaction among rational decision-makers.
#### markov property - the future is independent of the past given the present.

---

### minimax algorithm / depth doesn't change in our version of tic-tac-toe

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

### alpha-beta pruning / not useful for tic-tac-toe

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