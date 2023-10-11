### Introduction
- **Code to Show**: None

Hello everyone, today I'll be walking you through my project where I've implemented three different algorithms to play Tic-Tac-Toe: Value Iteration, Q-Learning, and Monte Carlo Tree Search. Let's dive right in!


---

## Value Iteration
- **Code to Show**: ValueIteration class and its methods

First up is Value Iteration. This algorithm treats Tic-Tac-Toe as a Markov Decision Process. I've created a ValueIteration class that inherits from an abstract Algorithm class. This class initializes the value function, policy, and a graph representing all possible game states.

### Value Function
**Code to Show**: The part of the ValueIteration class where the value function is initialized and updated.

The value function, often denoted as \( V(s) \), is a crucial component of Value Iteration. It assigns a numerical value to each state in the state space, representing the expected cumulative reward from that state when following an optimal policy. In the context of Tic-Tac-Toe, each unique board configuration is a state, and the value function estimates how "good" each configuration is for a player. The value function is initialized arbitrarily, often to zero, and is updated iteratively based on the rewards and transitions defined in the Markov Decision Process.

### Policy
Code to Show: The part of the ValueIteration class where the policy is initialized and updated.

The policy, denoted as \( \pi \), is essentially a strategy that the agent follows. It maps each state to an action that the agent will take when in that state. In our Tic-Tac-Toe game, the policy would specify the best move to make for any given board configuration. The policy is derived from the value function; it chooses the action that leads to the state with the highest value. As the value function converges to the optimal solution, so does the policy.

The most time-consuming part was creating the state space. I used a breadth-first search approach to explore all possible states and transitions. This ensures that the graph accurately represents the game's dynamics.

---

## Monte Carlo Tree Search (MCTS) - Four Main Steps

### Selection
- **Code to Show**: The `select` method in the `MonteCarloTreeSearch` class.

The selection step starts at the root node and traverses the tree by selecting the child node that maximizes a certain criterion until a leaf node is reached. The criterion often used is the Upper Confidence Bound for Trees (UCT), which balances exploration and exploitation. This ensures that the algorithm doesn't just stick to known paths but also explores new possibilities.

### Expansion
- **Code to Show**: The `expand` method in the `MonteCarloTreeSearch` class.

Once a leaf node is reached in the selection step, the expansion step adds one or more child nodes to the leaf node. These child nodes represent the various actions that can be taken from the state represented by the leaf node. In the context of Tic-Tac-Toe, this would mean adding child nodes for each empty cell on the board where a move can be made.

### Simulation
- **Code to Show**: The `simulate` method in the `MonteCarloTreeSearch` class.

After expansion, the simulation step is performed. Starting from the new leaf node, a simulation is run to a terminal state following a certain policy. In our implementation, we use the Q-Learning policy to guide the simulation. The outcome of this simulation provides an estimate of the value of the new node.

### Backpropagation
- **Code to Show**: The `backpropagate` method in the `MonteCarloTreeSearch` class.

The final step is backpropagation. Here, the algorithm traverses back up the tree from the new leaf node to the root, updating the value and visit count of each node along the way. This is done to ensure that the new information is incorporated into the tree, thereby improving the decision-making in future iterations.

### Q-Learning
- **Code to Show**: QLearning class and its methods

Next, we have Q-Learning. This is a model-free reinforcement learning algorithm that learns the value of an action in a particular state. It uses a Q-table to store these values and updates them as it explores more of the state space.

The Q-table is essentially a lookup table where we calculate the maximum expected future rewards for actions at each state. The algorithm iteratively updates the Q-values based on the rewards it receives, aiming to find an optimal policy over time. I've encapsulated this logic in a QLearning class.

In our Tic-Tac-Toe example, the Q-table would represent the value of placing a 'X' or 'O' in each cell for every possible board configuration. The QLearning class contains methods for updating these values based on the reward received after each move, which is how the algorithm learns to make better decisions.

These four steps in MCTS and the Q-Learning algorithm are repeated multiple times

---

### Integration and Challenges
- **Code to Show**: Integration class and its methods

Now, let's talk about how these algorithms are integrated. I've created an Integration class that uses Q-Learning as the primary decision-making algorithm but falls back to MCTS when Q-Learning is uncertain.

I did face some challenges, particularly in managing the current player during simulations in MCTS and ensuring the optimality of the Q-Learning policy.

---

### Conclusion and Future Work
- **Code to Show**: None

In conclusion, each algorithm has its strengths and weaknesses, but together they provide a robust and extensible architecture for playing Tic-Tac-Toe. There's room for improvement, and I plan to fine-tune the algorithms and complete the unfinished parts in the future. Thank you for watching!