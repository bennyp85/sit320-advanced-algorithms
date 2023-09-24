# Key Topics for SIT320 — Advanced Algorithms: MDP and RL Algorithms

---

## Table of Contents

1. [Overview of MDP (Markov Decision Processes)](#overview-of-mdp)
2. [Value-Iteration Algorithm](#value-iteration-algorithm)
3. [Q-Learning Algorithm](#q-learning-algorithm)
4. [Monte-Carlo Tree Search (MCTS)](#monte-carlo-tree-search)
5. [Tic-tac-toe Game Mechanics](#tic-tac-toe-game-mechanics)
6. [Limitations of Minimax Algorithm](#limitations-of-minimax-algorithm)
7. [Code Optimization Techniques](#code-optimization-techniques)
8. [Video Presentation Skills](#video-presentation-skills)

---

### Overview of MDP

### 1. States (S)
- **Definition**: A finite set of conditions or situations that the system can be in.
- **Example**: In a Tic-Tac-Toe game, each unique board configuration is a state.
- **Notation**: \( S = \{s_1, s_2, \ldots, s_n\} \)

### 2. Actions (A)
- **Definition**: A finite set of choices that can be made in each state.
- **Example**: In a Tic-Tac-Toe game, placing an 'X' or 'O' in an empty cell is an action.
- **Notation**: \( A = \{a_1, a_2, \ldots, a_m\} \)

### 3. Transition Model (P)
- **Definition**: Specifies the probability of reaching a new state \( s' \) from a current state \( s \) by taking action \( a \).
- **Example**: In a stochastic environment, there might be a 90% chance of moving north when the 'move north' action is chosen.
- **Notation**: \( P(s' | s, a) \)

### 4. Reward Function (R)
- **Definition**: Assigns a real number to each state-action-next_state triplet, indicating the immediate reward received.
- **Example**: In a Tic-Tac-Toe game, winning could give a reward of +1, losing -1, and a draw 0.
- **Notation**: \( R(s, a, s') \)

### 5. Policy (π)
- **Definition**: A strategy that specifies what action to take in each state.
- **Example**: In a Tic-Tac-Toe game, a policy might specify to place an 'X' in the center if it's empty.
- **Notation**: \( \pi(s) = a \)

### 6. Discount Factor (γ)
- **Definition**: A value between 0 and 1 that discounts future rewards.
- **Example**: A discount factor of 0.9 would make rewards received in the future worth 90% of immediate rewards.
- **Notation**: \( \gamma \)

### Objective
- **Optimal Policy (π*)**: The policy that maximizes the expected sum of discounted rewards over time.

### Equation
- **Bellman Equation**: 
  \[
  V(s) = \max_{a \in A} \left( R(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V(s') \right)
  \]


---

### Value-Iteration Algorithm

- Algorithm Steps
- Convergence Criteria
- Code Implementation

---

### Q-Learning Algorithm

- Exploration vs Exploitation
- Learning Rate and Discount Factor
- Temporal Difference Learning

---

### Monte-Carlo Tree Search (MCTS)

- Basic Principles
- Selection, Expansion, Simulation, and Backpropagation
- Integration with Q-Learning

---

### Tic-tac-toe Game Mechanics

- Board Representation
- Winning Conditions
- Move Generation

---

### Limitations of Minimax Algorithm in the Context of Tic-Tac-Toe, MDP, and RL

#### 1. Computational Complexity

- **General Issue**: Minimax involves searching through all possible game states, which can be computationally expensive.
- **Tic-Tac-Toe**: For a standard 3x3 board, the complexity is manageable, but for larger boards like 5x5 or 7x7, it becomes impractical.
- **MDP & RL**: In MDPs with large state spaces, using Minimax as a decision-making algorithm is often infeasible. RL algorithms like Q-Learning are generally more efficient.

#### 2. Lack of Randomness

- **General Issue**: Minimax is deterministic, always choosing the move that minimizes the worst-case scenario, making it predictable.
- **Tic-Tac-Toe**: An experienced player can easily counter Minimax moves, leading to frequent draws.
- **MDP & RL**: RL algorithms can incorporate randomness through exploration, making them more adaptable in stochastic environments.

#### 3. Pruning Techniques

- **General Issue**: Techniques like Alpha-Beta pruning are used to reduce the search space, but they also have limitations.
- **Tic-Tac-Toe**: Pruning can speed up the search on a 3x3 board but is still not sufficient for larger boards.
- **MDP & RL**: In MDPs, pruning is less straightforward due to the probabilistic nature of state transitions. RL algorithms like Monte-Carlo Tree Search offer more efficient ways to explore the state space.



---

### Code Optimization Techniques

- Dynamic Programming
- Memoization
- Parallel Computing

---

### Video Presentation Skills

- Script Preparation
- Visual Aids
- Time Management

