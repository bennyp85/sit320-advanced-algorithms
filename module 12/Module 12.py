# %% [markdown]
# # SIT320 Advanced Algorithms
# ## Module 12 - MDP and Reinforcement Learning

# %% [markdown]
# ---

# %% [markdown]
# ### Board Class

# %%
from abc import ABC, abstractmethod

class Board(ABC):
    def __init__(self, boardDimensions):
        self.boardDimensions = boardDimensions

    @abstractmethod
    def createBoard(self):
        pass

    @abstractmethod
    def printBoard(self):
        pass

    @abstractmethod
    def setCellState(self, position, state):
        pass

    @abstractmethod
    def getCellState(self, position):
        pass

    @abstractmethod
    def getBoardState(self):
        pass

    @abstractmethod
    def getBoardDimensions(self):
        pass

    @abstractmethod
    def spaceIsFree(self, position):
        pass

    

# %%
import itertools

class TicTacToeBoard(Board):
    def __init__(self, boardDimensions):
        """Create a board of dimensions boardDimensions x boardDimensions
        Args: boardDimensions (int): the dimensions of the board
        """
        self.boardDimensions = boardDimensions
        self.createBoard()


    def createBoard(self):
        """Create a board of dimensions boardDimensions x boardDimensions"""
        self.boardState = {i+1: ' ' for i in range(self.getBoardDimensions()**2)}

    def printBoard(self):
        for i in range(self.boardDimensions):
            row = [self.boardState[i*self.boardDimensions+j+1] for j in range(self.boardDimensions)]
            print('|'.join(row))
            if i < self.boardDimensions-1:
                print('-'*(self.boardDimensions*2-1))
        print('\n')

    def setCellState(self, position, state):
        """Set the state of a cell on the board
        Args:
            position (int): the position of the cell
            state (str): the state of the cell
        """
        self.boardState[position] = state

    def getCellState(self, position):
        """Get the state of a cell on the board
        Args:
            position (int): the position of the cell
        Returns: the state of the cell
        """
        return self.boardState[position]

    def getBoardState(self):
        """Get the state of the board
        Returns: A dictionary with keys 1 to boardDimensions**2 and values 'X', 'O' or ' '
        """
        return self.boardState

    def getBoardDimensions(self):
        """Get the dimensions of the board
        Returns: An integer representing the dimensions of the board 
        """
        return self.boardDimensions

    def getActions(self, state):
        """Get all valid actions for a given state."""
        return [
            i
            for i in range(1, self.boardDimensions**2 + 1)
            if state.getCellState(i) == ' '
        ]
    
    def spaceIsFree(self, position):
        if self.boardState[position] == ' ':
            return True

# %% [markdown]
# ---

# %% [markdown]
# ### Game Logic

# %%
from abc import ABC, abstractmethod

class GameLogic():
    def __init__(self, boardGame):
        self.boardGame = boardGame

    @abstractmethod
    def chkForkWin(self):
        pass

    @abstractmethod
    def chkForDraw(self):
        pass

    @abstractmethod
    def chkMarkForWin(self, letter):
        pass

# %%
class TicTacToeGameLogic(GameLogic):
    def __init__(self, boardGame):
        super().__init__(boardGame)
        """Create a game logic object for the board game
        Args: boardGame (Board): the board game. Must be a subclass of Board
        """

    def chkForDraw(self, state=None):
        """Check if the game is a draw.
        Returns: bool: True if the game is a draw, False otherwise.
        """
        if state is not None:
            boardState = state.getBoardState()
        else:
            boardState = self.boardGame.getBoardState()
        return all(boardState[key] != ' ' for key in boardState.keys())

    def chkForWin(self, state=None):
        """Check if any player has won.
        Returns: bool: True if any player has won, False otherwise.
        """
        # print('chkForWin')
        if state is not None:
            boardState = state.getBoardState()
            boardDimensions = state.getBoardDimensions()
        else:
            boardState = self.boardGame.getBoardState()
            boardDimensions = self.boardGame.getBoardDimensions()
        for i in range(boardDimensions):
            row = [boardState[i*boardDimensions+j+1] for j in range(boardDimensions)]
            if len(set(row)) == 1 and row[0] != ' ':
                return True
        for i in range(boardDimensions):
            column = [boardState[j*boardDimensions+i+1] for j in range(boardDimensions)]
            if len(set(column)) == 1 and column[0] != ' ':
                return True
        diagonal1 = [boardState[i*boardDimensions+i+1] for i in range(boardDimensions)]
        diagonal2 = [boardState[i*boardDimensions+(boardDimensions-i-1)+1] for i in range(boardDimensions)]
        if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
            return True
        return len(set(diagonal2)) == 1 and diagonal2[0] != ' '

    def chkMarkForWin(self, letter, state=None):
        """Check if the player with the specified letter has won.
        Args: letter (str): Letter of the player to check for win.
        Returns: bool: True if the player with the specified letter has won, False otherwise.
        """
        if state is not None:
            boardState = state.getBoardState()
            boardDimensions = state.getBoardDimensions()
        else:
            boardState = self.boardGame.getBoardState()
            boardDimensions = self.boardGame.getBoardDimensions()
        # check rows
        for i in range(boardDimensions):
            row = [boardState[i*boardDimensions+j+1] for j in range(boardDimensions)]
            if len(set(row)) == 1 and row[0] == letter:
                return True
        for i in range(boardDimensions):
            column = [boardState[j*boardDimensions+i+1] for j in range(boardDimensions)]
            if len(set(column)) == 1 and column[0] == letter:
                return True
        diagonal1 = [boardState[i*boardDimensions+i+1] for i in range(boardDimensions)]
        diagonal2 = [boardState[i*boardDimensions+(boardDimensions-i-1)+1] for i in range(boardDimensions)]
        if len(set(diagonal1)) == 1 and diagonal1[0] == letter:
            return True
        return len(set(diagonal2)) == 1 and diagonal2[0] == letter

# %% [markdown]
# ---

# %% [markdown]
# ### Player Classes

# %%
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, letter, algorithm):
        self.letter = letter
        self.algorithm = algorithm
        """Create a player object
        Args: letter (str): the letter of the player. Must be 'X' or 'O'
        Args: algorithm (Algorithm): the algorithm used by the player. Must be a subclass of Algorithm
        """


    @abstractmethod
    def makeMove(self, boardGame):
        pass

# %%
class HumanPlayer(Player):
    def __init__(self, letter, algorithm):
        self.letter = letter
        self.algorithm = algorithm
    
    # function for player to choose a position
    def makeMove(self, boardGame):
        """Make a move by asking for input from the user.
        Args: boardGame (Board): The board game object.
        If the position is not free, ask for another position.
        If the position is free, set the cell state to the player's letter.
        """
        position = self.algorithm.bestMove(boardGame, self.letter)
        boardGame.setCellState(position, self.letter)

# %%
class ComputerPlayer(Player):
    def __init__(self, letter, algorithm):
        self.letter = letter
        self.algorithm = algorithm
    
    def makeMove(self, boardGame):
        """Make a move by using the algorithm to find the best move.
        Args: boardGame (Board): The board game object.
        Set the cell state to the player's letter.
        """
        print('Computer is thinking...')
        position = self.algorithm.bestMove(boardGame, self.letter)
        print(f"Computer chose position: {position}")
        boardGame.setCellState(position, self.letter)

# %%
class UserInput(Algorithm):
    def __init__(self, boardGame):
        super().__init__(boardGame)

    def bestMove(self, boardGame, letter):
        """Ask the user for input.
        Args: boardGame (Board): The board game object.
        Args: letter (str): The letter of the computer player.
        Returns: int: The position of the user's input."""
        while True:
            try:
                position = int(input("Please enter a position: "))
                if position < 1 or position > boardGame.getBoardDimensions()**2:
                    raise ValueError
                if boardGame.spaceIsFree(position):
                    return position
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input!")

# %% [markdown]
# ### Game Factory Class

# %%
class AbstractGameFactory(ABC):

    @abstractmethod
    def createGameLogic(self) -> GameLogic:
        pass

    @abstractmethod
    def createPlayer(self) -> Player:
        pass

    @abstractmethod
    def createAlgorithm(self) -> Algorithm:
        pass

# %%
class TicTacToeCreator(AbstractGameFactory):
    def __init__(self, dimensions):
        self.board = TicTacToeBoard(dimensions)

    def createGameLogic(self) -> GameLogic:
        """Create a game logic object for the board game
        Returns: gameLogic (GameLogic): the game logic object. Must be a subclass of GameLogic
        """
        return TicTacToeGameLogic(self.board)

    def createPlayer(self, letter, isComputer, algorithm) -> Player:
        """Create a player object
        Args: letter (str): the letter of the player. Must be 'X' or 'O'
        Args: isComputer (bool): whether the player is a computer or not
        Args: algorithm (Algorithm): the algorithm used by the player. Must be a subclass of Algorithm
        Returns: player (Player): the player object. Must be a subclass of Player
        """
        if isComputer:
            return ComputerPlayer(letter, algorithm)
        return HumanPlayer(letter, algorithm)

    def createAlgorithm(self, algorithm) -> Algorithm:
        """Create an algorithm object for the board game
        Args: algorithm (int): the algorithm used by the player. Must be 1, 2, 3 or 4
        Returns: algorithm (Algorithm): the algorithm object. Must be a subclass of Algorithm
        """
        if algorithm == 1:
            return Minimax(self.board)
        elif algorithm == 2:
            return MinimaxAlphaBeta(self.board)
        elif algorithm == 3:
            return ValueIteration(self.board)
        elif algorithm == 4:
            return QLearning(self.board)
        elif algorithm == 5:
            q_learning_policy = model_manager.load_model(dimensions)
            return MonteCarloTreeSearch(self.board, q_learning_policy)
        elif algorithm == 6:
            return UserInput(self.board)

# %% [markdown]
# ---

# %% [markdown]
# ### Algorithm Classes

# %%
class Algorithm(ABC):
    def __init__(self, boardGame):
        self.boardGame = boardGame
        """Create an algorithm object for the board game
        Args: boardGame (Board): the board game. Must be a subclass of Board
        """
    
    @abstractmethod
    def bestMove(self, boardGame, letter):
        pass


# %% [markdown]
# ### MiniMax

# %%
class Minimax(Algorithm):
    def __init__(self, boardGame):
        super().__init__(boardGame)

    def bestMove(self, boardGame, letter):
        """Find the best move for the computer player.
        Args: boardGame (Board): The board game object
        Args: letter (str): The letter of the computer player.
        Returns: int: The position of the best move."""
        boardState = boardGame.getBoardState()
        bestScore = -1000
        bestMove = 0
        for key in boardState.keys():
            if boardState[key] == ' ':
                boardState[key] = letter
                score = self.minimax(boardState, 0, False, letter)
                boardState[key] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = key
        return bestMove

    def minimax(self, boardState, depth, isMaximizing, letter, maxDepth=5):
        """Find the best score for the computer player.
        Args: boardState (dict): The board state.
        Args: depth (int): The depth of the tree.
        Args: isMaximizing (bool): Whether the player is maximizing or not.
        Args: letter (str): The letter of the computer player.
        Args: maxDepth (int): The maximum depth of the tree.
        Returns: int: The best score for the computer player."""
        
        gameLogic = TicTacToeGameLogic(self.boardGame)
        opponentLetter = 'O' if letter == 'X' else 'X'
        if(gameLogic.chkMarkForWin(letter)):
            return 1
        elif(gameLogic.chkMarkForWin(opponentLetter)):
            return -1
        elif(gameLogic.chkForDraw()):
            return 0
        elif depth >= maxDepth:
            return 0

        if isMaximizing:
            bestScore = -1000
            for key in boardState.keys():
                if boardState[key] == ' ':
                    boardState[key] = letter
                    score = self.minimax(boardState, depth + 1, False, letter)
                    boardState[key] = ' '
                    if score > bestScore:
                        bestScore = score
        else:
            bestScore = 1000
            for key in boardState.keys():
                if boardState[key] == ' ':
                    boardState[key] = opponentLetter
                    score = self.minimax(boardState, depth + 1, True, letter)
                    boardState[key] = ' '
                    if score < bestScore:
                        bestScore = score
        return bestScore

# %% [markdown]
# ### Minimax with Alpha-Beta Pruning

# %%
class MinimaxAlphaBeta(Algorithm):
    def __init__(self, boardGame):
        super().__init__(boardGame)

    def bestMove(self, boardGame, letter):
        boardState = boardGame.getBoardState()
        bestScore = -1000
        bestMove = 0
        for key in boardState.keys():
            if boardState[key] == ' ':
                boardState[key] = letter
                score = self.minimax(boardState, 0, False, letter)
                boardState[key] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = key
        return bestMove

    def minimax(self, boardState, depth, isMaximizing, letter, alpha=-1000, beta=1000, maxDepth=5):
        """Find the best score for the computer player.
        Args: boardState (dict): The board state.
        Args: depth (int): The depth of the tree.
        Args: isMaximizing (bool): Whether the player is maximizing or not.
        Args: letter (str): The letter of the computer player.
        Args: alpha (int): The alpha value. 
        Args: beta (int): The beta value.
        Args: maxDepth (int): The maximum depth of the tree.
        Returns: int: The best score for the computer player."""
        gameLogic = TicTacToeGameLogic(self.boardGame)
        opponentLetter = 'O' if letter == 'X' else 'X'
        if(gameLogic.chkMarkForWin(letter)):
            return 1
        elif(gameLogic.chkMarkForWin(opponentLetter)):
            return -1
        elif(gameLogic.chkForDraw()):
            return 0
        elif depth >= maxDepth:
            return 0

        if isMaximizing:
            bestScore = -1000
            for key in boardState.keys():
                if boardState[key] == ' ':
                    boardState[key] = letter
                    score = self.minimax(boardState, depth+1, False, letter, alpha, beta)
                    boardState[key] = ' '
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        else:
            bestScore = 1000
            for key in boardState.keys():
                if boardState[key] == ' ':
                    boardState[key] = opponentLetter
                    score = self.minimax(boardState, depth+1, True, letter, alpha, beta)
                    boardState[key] = ' '
                    bestScore = min(score, bestScore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestScore

# %% [markdown]
# ---
# ### Reinforcement Learning
# --- 

# %% [markdown]
# 
# ### Value Iteration

# %%
import random
import copy

class ValueIteration(Algorithm):
    """ Value iteration algorithm for Tic Tac Toe
    Args: boardGame (Board): The board game object
    Initializes the value function, graph, and policy for the board game"""
    
    def __init__(self, boardGame):
        super().__init__(boardGame)
        self.policy =  {}
        self.G = Graph()
        self.value_function = {}
        self.valueIteration()


    def bestMove(self, boardGame, letter):
        """Find the best move for the computer player.
        Args: boardGame (Board): The board game object
        Args: letter (str): The letter of the computer player.
        Returns: int: The position of the best move."""

        boardState = boardGame.getBoardState()
        boardStateTuple = tuple(boardState.values())

        if action := self.policy.get(boardStateTuple, None):
            return self.extract_policy(action, boardStateTuple, boardState)
        else:
            print("No action found in policy for this state.")


    def extract_policy(self, action, boardStateTuple, boardState):
        """ Extract the policy given a state
        Args: action (int): The action to take
        Args: boardStateTuple (tuple): The board state as a tuple
        Args: boardState (dict): The board state as a dictionary
        Returns: int: The position of the best move."""

        print(f"Action found in policy: {action}")

        # Print the value of the current state
        current_state_value = self.value_function.get(boardStateTuple, "Unknown")
        print(f"Value of current state: {current_state_value}")

        # If you can calculate the next state, you can print its value too
        state_tuple = tuple(boardState.values())
        neighbors = self.G.get_neighbors(state_tuple)
        # print all the neighbors
        for neighbor in neighbors:
            print(f"Neighbor: {neighbor}")
            print(f"Value of neighbor: {self.value_function.get(neighbor, 'Unknown')}")

        # Print all possible actions and their values (if you have this information)
        # print(f"All possible actions and their values: {some_dictionary}")

        return action

            
    def valueIteration(self):
        """ Perform value iteration to find the optimal policy and value function"""

        game_logic = TicTacToeGameLogic(self.boardGame)
        best_policy = {}
        blankBoard = copy.deepcopy(self.boardGame)
        graph = self.initialize(self.G, blankBoard, game_logic)
        print("Graph initialized")
        self.value_function = {state: 0 for state in graph.nodes}
        if self.converge(game_logic):
            print("Converged")
        # print(f"Value function: {self.value_function}")


    def initialize(self, graph, board, game_logic):
        """ Initialize the graph with all possible states and actions
        Args: graph (Graph): The graph object
        Args: board (Board): The board object
        Args: game_logic (GameLogic): The game logic object
        Returns: Graph: The graph object with all possible states and actions"""
        print("Initializing...")
        print(f"Start state: {board.getBoardState()}")
        graph.add_node(tuple(board.getBoardState().values()))
        queue = [(board, 'X')]  # Add the player to the queue
        while queue:
            state, current_player = queue.pop(0)
            for action in board.getActions(state):
                new_state = copy.deepcopy(state)
                new_state.setCellState(action, current_player)
                new_state_tuple = tuple(new_state.getBoardState().values())
                
                edge_reward = 0  # Default edge reward
                
                # Check if the new state is a terminal state
                if game_logic.chkForWin(new_state):
                    graph.add_node(new_state_tuple)
                    if game_logic.chkMarkForWin('X', new_state):
                        edge_reward = 1
                        graph.nodes[new_state_tuple].value = 1
                    elif game_logic.chkMarkForWin('O', new_state):
                        edge_reward = -1
                        graph.nodes[new_state_tuple].value = -1
                    graph.add_edge(tuple(state.getBoardState().values()), new_state_tuple, edge_reward)
                    continue  # Skip adding this state to the queue
                elif game_logic.chkForDraw(new_state):
                    graph.add_node(new_state_tuple)
                    graph.nodes[new_state_tuple].value = 0
                
                if new_state_tuple not in graph.nodes:
                    graph.add_node(new_state_tuple)
                    next_player = 'O' if current_player == 'X' else 'X'
                    queue.append((new_state, next_player))
                
                graph.add_edge(tuple(state.getBoardState().values()), new_state_tuple, edge_reward)
                graph.update_edge_reward(tuple(state.getBoardState().values()), new_state_tuple)
        
        if not graph.nodes:
            raise ValueError("Graph is empty")
        return graph


    def converge(self, game_logic, gamma=0.9, epsilon=1e-4):
        """ Converges the value function and policy
        Args: game_logic (GameLogic): The game logic object
        Args: gamma (float): The discount factor
        Args: epsilon (float): The convergence factor (default 1e-4)
        Returns: bool: True if the value function converged, False otherwise"""
        print("Converging...")
        delta = float('inf')
        i = 0
        # Loop until the value function converges
        while delta > epsilon:
            delta = 0  # Reset delta for each iteration

            # Iterate through all states
            for curr_state in self.G.nodes.values():
                old_value = self.value_function.get(curr_state.state, 0)  # Get the old value function for the state
                best_action_value = self.calculateBestAction(curr_state.state, gamma)  # Calculate the best action value
                # print(f"Old value for state {curr_state.state}: {old_value}")
                # print(f"New value for state {curr_state.state}: {best_action_value}")

                # Update the value function
                self.value_function[curr_state.state] = best_action_value

                # Update the policy
                self.policy[curr_state.state] = self.calculateBestAction(curr_state.state, gamma, return_action=True)

                # Calculate the change in the value function for this state
                delta = max(delta, abs(old_value - best_action_value))
                # Inside the converge method
                # print(f"Delta: {delta}")  # To check the convergence value

            i += 1
        print(f"Number of iterations: {i}")

        print("Value function converged.")


    def calculateBestAction(self, state_tuple, gamma, return_action=False):
        """ Calculate the best action for a given state
        Args: state_tuple (tuple): The state as a tuple
        Args: gamma (float): The discount factor
        Args: return_action (bool): Whether to return the action or the value
        Returns: float: The value of the best action, or the best action itself"""

        max_value = float('-inf')  # Initialize to negative infinity
        best_action = None

        # Get the neighbors (possible next states) for the current state
        neighbors = self.G.get_neighbors(state_tuple)

        # If there are no neighbors, return 0 or None based on the flag
        if not neighbors:
            self.value_function[state_tuple] = 0  # Update value function for terminal states
            return 0 if not return_action else None

        # Initialize a list to store the best actions
        best_actions = []

        # Iterate through each neighbor to find the best action(s)
        for neighbor in neighbors:
            reward = self.G.get_reward(state_tuple, neighbor)
            value = reward + (gamma * self.value_function.get(neighbor, 0))  # Calculate the value of the action

            if value > max_value:
                max_value = value
                best_actions = [self.new_X_position(state_tuple, neighbor) + 1]  # Reset the list with the new best action
            elif value == max_value:
                best_actions.append(self.new_X_position(state_tuple, neighbor) + 1)  # Add this action to the list of best actions

        # Randomly choose one of the best actions
        best_action = random.choice(best_actions)

        # Update the value function for the current state
        self.value_function[state_tuple] = max_value

        return max_value if not return_action else best_action

    
    def new_X_position(self, state_tuple, chosen_neighbor):
        """ Get the position of the new X in the chosen neighbor
        Args: state_tuple (tuple): The state as a tuple
        Args: chosen_neighbor (tuple): The chosen neighbor as a tuple
        Returns: int: The position of the new X in the chosen neighbor"""
        return [
            i
            for i, (current, next) in enumerate(zip(state_tuple, chosen_neighbor))
            if current != next
        ][0]


# %%
class Node:
    def __init__(self, state, value):
        self.state = state
        self.value = value

    def __str__(self):
        return f"State: {self.state}, Value: {self.value}"

        

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, state, value=0):
        node = Node(state, value)
        self.nodes[state] = node
        return node

    def add_edge(self, state1, state2, reward=0):
        if state1 not in self.nodes:
            self.add_node(state1)
        if state2 not in self.nodes:
            self.add_node(state2)
        if state1 not in self.edges:
            self.edges[state1] = {}
        
        # Use the value of the destination node as the reward
        reward = self.nodes[state2].value if self.nodes[state2].value != 0 else reward
        # print(f"Reward: {reward}")
        self.edges[state1][state2] = reward

    def update_edge_reward(self, state1, state2):
        if state1 in self.edges and state2 in self.edges[state1]:
            self.edges[state1][state2] = self.nodes[state2].value
            # print(f"Updated edge reward: {self.edges[state1][state2]}")



    def get_neighbors(self, state):
        return [] if state not in self.edges else list(self.edges[state].keys())

    def get_reward(self, state1, state2):
        if state1 not in self.edges or state2 not in self.edges[state1]:
            return 0
        # print(self.edges[state1][state2])
        return self.edges[state1][state2]

    def print_graph(self):
        for i, node in enumerate(self.nodes.values(), start=1):
            print(f"State {i} Node: {node}")
            neighbors = self.get_neighbors(node.state)
            for neighbor in neighbors:
                reward = self.get_reward(node.state, neighbor)
                print(f"  -> State {self.get_node_index(neighbor)} (Reward={reward})")

    # def get_node_index(self, state):
    #     return list(self.nodes.keys()).index(state) + 1

    # def count_winning_states(self):
    #     return sum(1 for node in self.nodes.values() if node.value == 1)
    
    # def count_losing_states(self):
    #     return sum(1 for node in self.nodes.values() if node.value == -1)

    # def count_draw_states(self):
    #     return sum(1 for node in self.nodes.values() if node.value == 0)


# %% [markdown]
# ### Q-Learning

# %%
import copy
import random
class QLearning(Algorithm):
    def __init__(self, boardGame, policy=None, explorationRate=0.2, learningRate=0.5, discountFactor=0.9):
        super().__init__(boardGame)
        self.boardGame = boardGame
        self.game_logic = TicTacToeGameLogic(self.boardGame)
        self.Qvalues = {}
        self.explorationRate = explorationRate
        self.learningRate = learningRate
        self.discountFactor = discountFactor
        if policy is None:
            self.policy = {}
            self.train(300)
        else:
            self.policy = policy



    def export_policy(self) -> dict:
        return self.policy


    def bestMove(self, boardGame, letter):
        """Find the best move for the computer player.
        Args: boardGame (Board): The board game object
        Args: letter (str): The letter of the computer player.
        Returns: int: The position of the best move."""

        boardState = boardGame.getBoardState()
        print(f"Board state: {boardState}")
        boardStateTuple = tuple(boardState.values())

        if action := self.policy.get(boardStateTuple, None):
            return self.extract_policy(action, boardStateTuple, boardState)
        print("No action found in policy for this state.")
        # Fallback policy: Choose a random available action
        possible_actions = [
            i + 1
            for i in range(boardGame.getBoardDimensions() ** 2)
            if boardGame.getCellState(i + 1) == ' '
        ]
        return random.choice(possible_actions)  # or some heuristic



    def extract_policy(self, action, boardStateTuple, boardState):
        """Extract the best move from the policy.
        Args:
            action (int): The action suggested by the policy.
            boardStateTuple (tuple): The tuple representation of the board state.
            boardState (dict): The dictionary representation of the board state.
        Returns:
            int: The position of the best move.
        """
        if boardState[action] == ' ':
            return action
    

    def qLearning(self):
    # Entry point for the Q learning algorithm
        current_state = self.boardGame
        player_queue = ['X']
        while not self.game_logic.chkForWin(current_state) and not self.game_logic.chkForDraw(current_state):
            action = self.chooseAction(current_state, self.explorationRate)
            # current_state.printBoard()
            # print(f"Action: {action}")
            current_player = player_queue.pop(0)
            # print(f"Current player: {current_player}")
            new_state, next_player = self.takeAction(current_state, action, current_player)
            reward = self.observeReward(new_state)  # Call observeReward here
            # print(f"new state: {new_state.getBoardState()}")
            self.updateQValues(current_state, action, reward, new_state)  # Assume you'll implement this method to update Q-values
            player_queue.append(next_player)
            current_state = new_state
            # current_state.printBoard()
        # print("Game over")
        # for values in self.Qvalues:
        #     print(f"State: {values[0].getBoardState()}, Action: {values[1]}, Q value: {self.Qvalues[values]}")



    def chooseAction(self, current_state, explorationRate):
        """Choose an action based on the current state and exploration rate
        Args: current_state (Board): The current state of the board
        Args: explorationRate (float): The exploration rate
        Returns: int: The action to take"""

        possible_actions = [
            i + 1
            for i in range(current_state.getBoardDimensions() ** 2)
            if current_state.getCellState(i + 1) == ' '
        ]
        # print(f"Possible actions: {possible_actions}")
        random_value = random.uniform(0, 1)
        if random_value < explorationRate:
            return random.choice(possible_actions)
        # negative infinity
        max_q_value = float('-inf')
        best_action = []
        for action in possible_actions:
            # print(f"Action: {action}")
            # if current state, action is not in q values, set it to 0
            if (current_state, action) not in self.Qvalues:
                # print(f"State: {current_state.getBoardState()}, Action: {action} not in Q values")
                self.Qvalues[(current_state, action)] = 0
                # print(f"Q value: {self.Qvalues[(current_state, action)]}")
                # get q value for current state, action
            q_value = self.Qvalues[(current_state, action)]
            if q_value > max_q_value:
                max_q_value = q_value
                best_action = [action]
            elif q_value == max_q_value:
                best_action.append(action)
        return random.choice(best_action)


    def takeAction(self, current_state, action, current_player):

        new_state = copy.deepcopy(current_state)
        new_state.setCellState(action, current_player)
        # swap player
        next_player = 'O' if current_player == 'X' else 'X'
        return new_state, next_player



    def observeReward(self, new_state):
        LOSE_REWARD = -1
        DRAW_REWARD = 0

        if self.game_logic.chkMarkForWin('X', new_state):
            # print("X wins")
            return 1
        elif self.game_logic.chkMarkForWin('O', new_state):
            # print("O wins")
            return LOSE_REWARD
        elif self.game_logic.chkForDraw(new_state):
            # print("Draw")
            return DRAW_REWARD
        else:
            return 0


    def updateQValues(self, current_state, action, reward, new_state):
    # Step 1: Get current Q-value
        current_q_value = self.Qvalues.get((current_state, action), 0)
        # print(f"Current Q value: {current_q_value}")
        # print(f"current state: {current_state.getBoardState()}")

        # Step 2: Get max Q-value for new state
        possible_actions_new_state = [
            i + 1
            for i in range(current_state.getBoardDimensions() ** 2)
            if current_state.getCellState(i + 1) == ' '
        ]

        max_new_state_value = max(
            self.Qvalues.get((new_state, a), 0) for a in possible_actions_new_state
        )

        # If new_state is terminal, set max_new_state_value to 0
        if self.game_logic.chkForWin(new_state) or self.game_logic.chkForDraw(new_state):
            max_new_state_value = 0

        # Step 3: Update Q-value using Q-Learning formula
        updated_q_value = (1 - self.learningRate) * current_q_value + self.learningRate * (reward + self.discountFactor * max_new_state_value)

        # Update the Q-value in the dictionary
        self.Qvalues[(current_state, action)] = updated_q_value
        # print(f"Updated Q value: {updated_q_value}")



    def updatePolicy(self):
        for state, _ in self.Qvalues.keys():
            # Convert the TicTacToeBoard object to a tuple
            state_tuple = tuple(state.getBoardState().values())
            
            possible_actions = [
                i + 1
                for i in range(state.getBoardDimensions() ** 2)
                if state.getCellState(i + 1) == ' '
            ]
            
            # Update the policy using the tuple representation of the state
            self.policy[state_tuple] = max(
                (
                    (action, self.Qvalues.get((state, action), 0))
                    for action in possible_actions
                ),
                key=lambda x: x[1],
            )[0]
            
        # print("Policy updated")



    def train(self, num_episodes):
        for _ in range(num_episodes):
            self.qLearning()
            self.updatePolicy()
        print("Training complete")


    def checkConvergence(self):
        pass

# %%
import pickle

class ModelManager:
    def __init__(self):
        self.models = {}

    def load_model(self, dimensions):
        if dimensions not in self.models:
            try:
                with open(f'qlearning_{dimensions}x{dimensions}.pkl', 'rb') as f:
                    self.models[dimensions] = pickle.load(f)
            except FileNotFoundError:
                print(f"No pre-trained model found for {dimensions}x{dimensions}. Training now...")
                self.train_and_save_model(dimensions)
        return self.models[dimensions]

    def train_and_save_model(self, dimensions):
        game_factory = TicTacToeCreator(dimensions)
        initial_board = game_factory.board  # Assuming this gives you the initial board
        q_learning_instance = QLearning(initial_board, policy=None, explorationRate=0.2, learningRate=0.5, discountFactor=0.9)
        q_learning_policy = q_learning_instance.export_policy()
        
        with open(f'qlearning_{dimensions}x{dimensions}.pkl', 'wb') as f:
            pickle.dump(q_learning_policy, f)
        
        self.models[dimensions] = q_learning_policy
        print(f"Trained and saved Q-Learning policy for {dimensions}x{dimensions} board.")

# Initialize the ModelManager
model_manager = ModelManager()

# Train and save models for 3x3, 4x4, and 5x5 boards
for dimensions in [3, 4, 5]:
    # check if model exists
    if model_manager.load_model(dimensions):
        continue
    model_manager.train_and_save_model(dimensions)

# %% [markdown]
# ### Monte Carlo Tree Search

# %%
from typing import List, Any

class TreeNode:
    """
    A node in the MCTS tree.
    Each node keeps track of its own value Q, prior probability P, and
    its visit-count-adjusted prior score u.
    """
    def __init__(self, state: Any, parent: 'TreeNode', visit_count: int, value: float, action: Any = None):
        self.state = state
        self.parent = parent
        self.visit_count = visit_count
        self.value = value
        self.action = action
        self.children: List[TreeNode] = []
        # print(f"TreeNode initialized with state type: {type(self.state)}, content: {self.state.getBoardState() if self.state else None}")


    def __str__(self) -> str:
        return f"State: {self.state}, Visit Count: {self.visit_count}, Value: {self.value}"

class Tree:
    """
    A tree in the MCTS algorithm.
    """
    def __init__(self):
        self.root: TreeNode = None

    def set_root(self, state: Any):
        self.root = TreeNode(state, None, 0, 0)

    def add_child(self, parent: TreeNode, state: Any, action: Any) -> TreeNode:
        node = TreeNode(state, parent, 0, 0, action)
        parent.children.append(node)
        return node

    def get_action(self, node: TreeNode) -> Any:
        return node.action

    def get_node(self, state: Any) -> TreeNode:
        return self._get_node(state, self.root)

    def get_state(self, node: TreeNode) -> Any:
        # print(f"Retrieved state type: {type(node.state)}, content: {node.state}")
        return node.state
    
    def get_root(self) -> TreeNode:
        return self.root

    def get_children(self, node: TreeNode) -> List[TreeNode]:
        # print(f"Retrieved children type: {type(node.children)}, content: {node.children}")
        return node.children
    
    def get_parent(self, node: TreeNode) -> TreeNode:
        return node.parent

    def get_visit_count(self, node: TreeNode) -> int:
        return node.visit_count

    def get_value(self, node: TreeNode) -> float:
        return node.value

    def increment_visit_count(self, node: TreeNode):
        node.visit_count += 1
        
    def add_value(self, node: TreeNode, value: float):
        node.value = value

# %%
from typing import Any
from collections import deque

class MonteCarloTreeSearch(Algorithm):
    """
    Monte Carlo Tree Search algorithm for Tic Tac Toe
    """
    def __init__(self, board_game: Any, q_learning_policy: dict, simulation_limit: int = 100, exploration_constant: float = 1.414):
        super().__init__(board_game)
        self.tree = Tree()
        self.tree.set_root(board_game)
        self.game_logic = TicTacToeGameLogic(board_game)
        self.policy = q_learning_policy  # Importing the Q-Learning policy
        self.q_values = {}
        self.simulation_count = 0
        self.simulation_limit = simulation_limit
        self.exploration_constant = exploration_constant
        self.player_queue = deque(['X', 'O'])

    def bestMove(self, boardGame: Board, letter: str) -> int:
        """Find the best move for the computer player.
        Args: boardGame (Board): The board game object
        Args: letter (str): The letter of the computer player.
        Returns: int: The position of the best move.
        """

        boardState = boardGame.getBoardState()
        boardStateTuple = tuple(boardState.values())

        # Check if the current state exists in the policy
        if action := self.policy.get(boardStateTuple, None):
            return self.extract_policy(action, boardStateTuple, boardState)

        # Fallback policy: Choose a random available action
        possible_actions = [
            i + 1
            for i in range(boardGame.getBoardDimensions() ** 2)
            if boardGame.getCellState(i + 1) == ' '
        ]
        return random.choice(possible_actions)  # or some other heuristic

        

    def extract_policy(self, action, boardStateTuple, boardState):
        """Extract the best move from the policy.
        Args:
            action (int): The action suggested by the policy.
            boardStateTuple (tuple): The tuple representation of the board state.
            boardState (dict): The dictionary representation of the board state.
        Returns:
            int: The position of the best move.
        """
        if boardState[action] == ' ':
            return action


    def import_ql_policy(self, q_learning_policy: dict):
        """ 
        Import the Q-Learning policy
        """
        self.policy = q_learning_policy

    def select(self):
        current_node = self.tree.get_root()  # Start at the root node
        while not self.is_leaf_node(current_node):
            children = self.tree.get_children(current_node)
            # Use UCT to select the best child node to explore
            best_child = max(children, key=lambda child: self.uct_value(current_node, child))
            current_node = best_child
        return current_node  # Return the leaf node for expansion

    def uct_value(self, parent, child):
        w = self.tree.get_value(child)  # Total reward of the node
        n = self.tree.get_visit_count(child)  # Number of times the node has been visited
        N = self.tree.get_visit_count(parent)  # Number of times the parent has been visited
        
        # Avoid division by zero
        if n == 0:
            return float('inf')
        
        # print type of child
        # print(f"Child type: {type(child)}")
        # print(f"w: {w}, n: {n}, N: {N}")
        return w / n + self.exploration_constant * ((N / n) ** 0.5)

    def is_leaf_node(self, node):
        return len(self.tree.get_children(node)) == 0



    def expand(self, node):
        """
        Expand the tree by adding new nodes based on possible actions.
        """
        # print("Expanding...")
        current_state = self.tree.get_state(node)  # Assuming get_state returns a TicTacToeBoard object
        board_dimension = current_state.getBoardDimensions()
        
        possible_actions = [
            i + 1
            for i in range(board_dimension ** 2)
            if current_state.getCellState(i + 1) == ' '
        ]
        
        for action in possible_actions:
            new_state = copy.deepcopy(current_state)
            
            # Debugging setCellState
            returned_state = new_state.setCellState(action, "X") 
            # Add the new state as a child node
            new_node = self.tree.add_child(node, new_state, action)
            


    def is_terminal_state(self, state):
        return self.game_logic.chkForDraw(state) or self.game_logic.chkForWin(state)


    def simulate(self, node):
        """
        Use Q-Learning policy to simulate the game from the given node to a terminal state.
        """
        # print("Simulating...")
        current_state = self.tree.get_state(node)
        local_player_queue = deque(['O', 'X'])
        # Ensure that the node's state is a TicTacToeBoard object
        if not isinstance(current_state, TicTacToeBoard):
            raise ValueError("Node's state must be a TicTacToeBoard object.")
            
        while not self.is_terminal_state(current_state):
            # Use Q-Learning policy to choose an action
            current_player = local_player_queue.popleft()
            state_str = str(current_state.getBoardState())  # Convert the board state to a string or some hashable form
            if state_str in self.policy:
                action = max(self.policy[state_str], key=self.policy[state_str].get)  # Choose the action with the highest Q-value
            else:
                # If the state is not in the policy, choose a random action
                possible_actions = [
                    i + 1
                    for i in range(current_state.getBoardDimensions() ** 2)
                    if current_state.getCellState(i + 1) == ' '
                ]
                action = random.choice(possible_actions)
            
            new_state = copy.deepcopy(current_state)
            new_state.setCellState(action, current_player)
            local_player_queue.append(current_player)
            current_state = new_state

        # At the end of the while loop, you have a terminal state in `current_state`
        reward = 0  # Initialize reward
        if self.game_logic.chkMarkForWin('X', current_state) and self.game_logic.chkForWin(current_state):
            # print("X wins")
            reward = 1
        elif self.game_logic.chkMarkForWin('O', current_state) and self.game_logic.chkForWin(current_state):
            # print("O wins")
            reward = -1
        elif self.game_logic.chkForDraw(current_state):
            # print("Draw")
            reward = 0
        # print(f"Reward: {reward}")
        return reward



    def backpropagate(self, leaf_node, reward):
        current_node = leaf_node  # Start at the leaf node
        while current_node is not None:  # Traverse back to the root
            self.tree.increment_visit_count(current_node)  # Increment the visit_count of the current node
            self.tree.add_value(current_node, reward)  # Update the value of the current node based on the reward

            # Check if the current node is the root
            if current_node == self.tree.get_root():
                break  # Stop backpropagation if you've reached the root

            current_node = self.tree.get_parent(current_node)  # Move to the parent node
            # print(f"Current node in backpropagate: Type - {type(current_node)}, Content - {current_node.state.getBoardState() if current_node else None}")





# %%
from typing import Any, List, Optional, Deque
from collections import deque

class Integration:
    def __init__(self, 
                 mcts_instance: MonteCarloTreeSearch, 
                 q_learning_instance: QLearning, 
                 board_game: Any, 
                 simulation_limit: int = 10, 
                 exploration_constant: float = 1.414):
        """
        Initialize the integration class with instances of MonteCarloTreeSearch and QLearning.
        
        Parameters:
            mcts_instance: An instance of MonteCarloTreeSearch.
            q_learning_instance: An instance of QLearning.
            board_game: The initial board state.
            simulation_limit: The limit for MCTS simulations.
            exploration_constant: The exploration constant for MCTS.
        """
        self.mcts = mcts_instance
        self.q_learning = q_learning_instance
        self.board_game = board_game
        self.simulation_limit = simulation_limit
        self.exploration_constant = exploration_constant
        self.player_queue = deque(['X', 'O'])

    def initialize(self) -> None:
        """
        Initialize the mcts tree with the root as the current board state.
        """
        self.mcts.tree.set_root(self.board_game)
        print("Initialized")

    def action_selection(self) -> Any:
        """
        Use Q-Learning policy to select an action, but use MCTS for states where q-learning is uncertain.
        
        Returns:
            The selected action.
        """
        # Step 1: Retrieve Current State
        current_state = self.board_game.getBoardState()

        # Step 2: Q-Learning Action
        q_learning_action = self.q_learning.bestMove(self.board_game, self.player_queue[0])  # Assuming 'X' is the current player

        if is_uncertain := self.check_uncertainty(
            current_state, q_learning_action
        ):
            mcts_action = self.mcts_action(current_state)
            return mcts_action

        # Step 5: Return Action
        return q_learning_action

    def check_uncertainty(self, current_state, q_learning_action) -> bool:
        """
        Check if Q-Learning is uncertain about the chosen action.
        
        Args:
            current_state: The current board state.
            q_learning_action: The action chosen by Q-Learning.
            
        Returns:
            bool: True if uncertain, False otherwise.
        """
        # Step 1: Retrieve Q-Values
        possible_actions = [
            i + 1
            for i in range(self.board_game.getBoardDimensions() ** 2)
            if self.board_game.getCellState(i + 1) == ' '
        ]
        q_values = [self.q_learning.Qvalues.get((current_state, action), 0) for action in possible_actions]
        
        # Step 2: Check for Multiple Maxima
        max_q_value = max(q_values)
        count_max_q_value = q_values.count(max_q_value)
        
        # Step 3: Return Uncertainty Status
        return count_max_q_value > 1


    def mcts_action(self, current_state) -> Any:
        # Step 1: Initialize the Tree's Root
        self.mcts.tree.set_root(current_state)
        
        # Step 2: Run Simulations
        for _ in range(self.simulation_limit):
            leaf_node = self.mcts.select()
            self.mcts.expand(leaf_node)
            reward = self.mcts.simulate(leaf_node)
            self.mcts.backpropagate(leaf_node, reward)

      
        # Step 3: Choose Best Action
        root = self.mcts.tree.get_root()
        children = self.mcts.tree.get_children(root)
        
        if not children:
            raise ValueError("No children found for the root node.")
        
        # Handle zero-division error
        best_child = max(children, key=lambda child: self.mcts.tree.get_value(child) / self.mcts.tree.get_visit_count(child) if self.mcts.tree.get_visit_count(child) != 0 else 0)
        
        return self.mcts.tree.get_action(best_child)







    def tree_update(self, action_taken) -> None:
        """
        Update the tree based on the latest action and state.
        """
        current_root = self.mcts.tree.get_root()

        # Find the new root based on the action taken
        children = self.mcts.tree.get_children(current_root)
        new_root = next(
            (
                child
                for child in children
                if self.mcts.tree.get_action(child) == action_taken
            ),
            None,
        )
        if new_root is None:
            raise ValueError("Action taken does not correspond to any child of the current root.")

        # Prune the tree by setting the new root
        # print(f"New root type: {type(new_root.state.getBoardState())}")
        self.mcts.tree.set_root(new_root)
        return new_root
        


    def policy_update(self) -> None:
        """
        Update the policy based on the latest action and state.
        """
        # TODO: Implement policy update logic
        pass

    def efficiency_guide(self) -> Optional[List[Any]]:
        """
        Provide guidance or metrics for improving the efficiency of the algorithms.
        
        Returns:
            A list of suggestions or metrics, or None.
        """
        # TODO: Implement efficiency guide logic
        pass


# %%
q_learning_policy = model_manager.load_model(5)
# print(f"Q-Learning policy for 3x3 board: {q_learning_policy}")

# with open('qlearning_3x3.pkl', 'rb') as f:
#     data = pickle.load(f)
# print(data)


if q_learning_policy is not None:
    # Initialize the TicTacToeCreator and QLearning instances
    game_factory = TicTacToeCreator(5)
    initial_board = game_factory.board  # Assuming this gives you the initial board
    q_learning_instance = QLearning(boardGame=initial_board, policy=q_learning_policy, learningRate=0.5) # Assuming this sets the policy

    # Initialize the MonteCarloTreeSearch instance
    mcts_instance = MonteCarloTreeSearch(initial_board, q_learning_policy)

    # Initialize the Integration instance
    integration_instance = Integration(mcts_instance, q_learning_instance, initial_board)

    # Initialize the Integration class
    integration_instance.initialize()

    # Test the mcts_action function
    best_action = integration_instance.mcts_action(initial_board)
    print(f"Best action determined by MCTS: {best_action}")

    new_root = integration_instance.tree_update(best_action)
    print("Done")
else:
    print("Could not load the model. Please train it first.")

# %% [markdown]
# ---

# %% [markdown]
# ## Game Loop

# %%
import time

def prompt_user(prompt, options):
    """Prompt the user to choose an option.
    Args: prompt (str): The prompt to display to the user.
    Args: options (list): The list of options to display to the user.
    Returns: int: The option chosen by the user.
    """
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = int(input("Please choose an option: "))
    while choice < 1 or choice > len(options):
        print(f"Choice must be between 1 and {len(options)}!")
        choice = int(input("Please choose an option: "))
    return choice

def choose_game():
    """Prompt the user to choose a game.
    Returns: game_factory (AbstractGameFactory): The game factory for the game chosen by the user.
    """
    prompt = "Welcome to the Game Factory!\nPlease choose a game:"
    options = ["Tic Tac Toe", "Chess", "Backgammon"]
    choice = prompt_user(prompt, options)
    if choice == 1:
        dimensions = int(input("Please enter the board dimensions: "))
        return TicTacToeCreator(dimensions)
    elif choice == 2:
        return ChessCreator()
    elif choice == 3:
        return BackgammonCreator()

def choose_algorithm():
    """Prompt the user to choose an algorithm.
    Returns: int: The algorithm chosen by the user.
    """
    prompt = "Which Algorithm should player use?"
    options = ["Minimax", "Minimax with Alpha Beta Pruning", "Value Iteration", "Q-Learning", "MCTS", "User Input"]
    return prompt_user(prompt, options)

def create_player(game_factory, letter):
    """Create a player object
    Args: game_factory (AbstractGameFactory): The game factory for the game chosen by the user.
    Args: letter (str): the letter of the player. Must be 'X' or 'O'
    Returns: player (Player): the player object. Must be a subclass of Player
    """
    is_computer = input(f"Is player {letter} a computer? (Y/N): ")
    while is_computer not in ['Y', 'N']:
        print("Invalid input!")
        is_computer = input(f"Is player {letter} a computer? (Y/N): ")
    algorithm_choice = choose_algorithm()
    algorithm = game_factory.createAlgorithm(algorithm_choice)
    return game_factory.createPlayer(letter, is_computer == 'Y', algorithm)

def play_game():
    """Play the game."""
    game_factory = choose_game()
    game_logic = game_factory.createGameLogic()
    player_one = create_player(game_factory, 'X')
    player_two = create_player(game_factory, 'O')
    game_factory.board.printBoard()
    start = time.time()
    while not game_logic.chkForWin() and not game_logic.chkForDraw():
        player_one.makeMove(game_factory.board)
        game_factory.board.printBoard()
        if game_logic.chkForWin():
            print("Player", player_one.letter, "wins!")
            end = time.time()
            print("Time taken: ", end - start)
            break
        elif game_logic.chkForDraw():
            print("It's a draw!")
            end = time.time()
            print("Time taken: ", end - start)
            break
        player_two.makeMove(game_factory.board)
        game_factory.board.printBoard()
        if game_logic.chkForWin():
            print("Player", player_two.letter, "wins!")
            end = time.time()
            print("Time taken: ", end - start)
            break
        elif game_logic.chkForDraw():
            print("It's a draw!")
            end = time.time()
            print("Time taken: ", end - start)
            break

play_game()


