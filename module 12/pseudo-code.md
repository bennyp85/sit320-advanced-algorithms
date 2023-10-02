## chooseAction()
```
1. Input: current_state, explorationRate (ε)
2. Output: selected_action

3. Initialize an empty list called 'possible_actions'

4. Use the 'getActions()' method from the TicTacToeBoard class to get all possible actions for the current_state
    - Add these actions to 'possible_actions'

5. Generate a random number between 0 and 1, call it 'random_value'

6. IF 'random_value' < explorationRate (ε) THEN
    6.1 Randomly select an action from 'possible_actions'
    6.2 Return the selected action

7. ELSE
    7.1 Initialize 'max_Q_value' as negative infinity and 'best_actions' as an empty list
    7.2 FOR each action in 'possible_actions'
        7.2.1 IF (current_state, action) is not in Qvalues, initialize it to 0
        7.2.2 Get Q_value for (current_state, action) from Qvalues
        7.2.3 IF Q_value > max_Q_value THEN
            7.2.3.1 Set 'max_Q_value' to Q_value
            7.2.3.2 Clear 'best_actions' list and add this action to it
        7.2.4 ELSE IF Q_value == max_Q_value THEN
            7.2.4.1 Add this action to 'best_actions'
    7.3 Randomly select an action from 'best_actions'
    7.4 Return the selected action

```