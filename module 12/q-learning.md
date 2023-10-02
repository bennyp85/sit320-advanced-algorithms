## Understanding the Algorithm: Q-Learning

### Basic Concepts
- **Q-Value**: Represents the quality of an action taken from a particular state.
- **State**: A configuration of the Tic-Tac-Toe board.
- **Action**: Placing a 'X' or 'O' in an empty cell.
- **Reward**: Numerical value received after performing an action. In Tic-Tac-Toe, this could be +1 for a win, -1 for a loss, and 0 otherwise.
- **Policy**: A strategy that the agent employs to determine the next action based on the current state.

### Equation
The Q-value is updated using the equation:

\[
Q(s, a) \leftarrow (1 - \alpha) \times Q(s, a) + \alpha \times \left( r + \gamma \times \max_{a'} Q(s', a') \right)
\]

Where:
- \( s \) = current state
- \( a \) = action taken
- \( r \) = reward received
- \( s' \) = next state
- \( a' \) = next action
- \( \alpha \) = learning rate
- \( \gamma \) = discount factor

### Differences from Value Iteration
- **Online Learning**: Unlike Value Iteration, which is model-based and requires knowledge of all possible states beforehand, Q-Learning is model-free and learns by interacting with the environment.
- **Exploration-Exploitation**: Q-Learning often uses strategies like ε-greedy to balance exploration and exploitation, which is not a concern in Value Iteration.

## Design and Architecture

### Identify Components
1. **State Representation**: You can reuse the state representation from your Value Iteration code.
2. **Action Selection**: Implement ε-greedy or another strategy for action selection.
3. **Q-Value Updates**: Code to update the Q-values based on the equation above.

### Reuse Code
- State representation, reward structure, and game termination checks can be reused from your Value Iteration code.

### Pseudocode
```python
Initialize Q-values to zeros or small random numbers
for each episode:
    Initialize state s
    while s is not terminal:
        Choose action a using ε-greedy from Q-values
        Take action a, observe reward r and next state s'
        Update Q-value for the state-action pair (s, a)
        s = s'
```
## Pre-Implementation Steps
**Data Structures**: A dictionary can be used to store Q-values, where the key is a tuple (state, action).
**Initialize Q-Values**: Initialize to zeros or small random numbers.
**Exploration vs Exploitation**: Implement ε-greedy strategy for action selection.