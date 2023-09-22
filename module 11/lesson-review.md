# SIT320 - Advanced Algorithms
## Credit Task 11: Network-based Algorithms
### School of Information Technology, Deakin University

## Overview of Learning (Module Summary)
[GitHub Link](https://github.com/bennyp85/sit320-advanced-algorithms/tree/master/module%2011)
[ChatGPT](https://chat.openai.com/share/141f13b0-f4ba-47e3-9253-688a1542501e)

Flow algorithms are used to solve problems that can be represented as a network of nodes and edges. Networks can be represented by the use of directed graphs.
In this module we were given two tasks to complete. The first task was to implement Karger's algorithm with the addition of weighted edges. The second task was to implement the Ford-Fulkerson algorithm to find the maximum flow in a network.
I will demostrate that finding the maximum flow in a network is equivalent to finding the minimum cut of a network.

## Problem 1: Karger's Algorithm with Weighted Edges

### Problem Statement
If we are presented with a network that includes weighted edges how would we modify Karger's algorithm to find the minimum cut of the network?
Karger's algorithm is a randomized algorithm that can be used to find the minimum cut of a network. 
The minimum cut is the smallest number of edges that need to be removed to disconnect the network.

### Assumptions
We can assume that all edge weights are non-negative intergers and are chosen randomly from the range [1, 10].
The graph will be connected and not contain any self-loops.

### Solution
I will be going off the asumption that **90% correct** is an acceptable accuracy for the algorithm.
This value was chosen as it is very close to one iteration(!) of the Kargers4 algorithm.
I ran the first two algorithms **(n * (n - 1) / 2 * log(1 / 0.1)) times** and returned the minimum cut found.
1. Karger's with random edge weights and contraction chosen probabilistically -> SLOW O(n^4) and ACCURATE with high number of iterations
2. Karger's with no edge weights and contraction chosen randomly -> SLOW O(n^4) and ACCURATE with high number of iterations
3. Recursive version of Karager's with the no edge weights -> FAST O(n^2 log^3 n) and ACCURATE with ONE iteration

I chose to implment a **probabilistic version** of Karger's algorithm with weighted edges as my solution to the task. I was originally puzzled about how weights could help us find the minimum cut of a network with Karger's algorith. I was fixated on the idea that I **needed to know** with some certainty **where** the minimum cut was. Karger's finds edges to contract randomly and my solution to implement probabilities to chose an edge to contract is essentially doing the same thing.


### Key Take aways
I believe that the idea of this task was a way to lead us to the Ford-Fulkerson algorithm. Adding weights to Karger's algorithm did not lead to any insights, but rather allowed me to appriciate the ideas presented in the next task. I feel as if we posses the knowledge of where the minimum cut is, we can manipulate the weights of the edges closest to find thesolution more efficiently. There have been improvements in Karger's algorithm, and I attempted to implement these improvments. *see Kargers4* in the notebook.

### Randomised Algorithms
Karger's is an example of a monte carlo algorithm. It is a randomized algorithm in the sense that it uses randomisation to decide what to do next. To find a solution with any certainty, the algorithm must be run multiple times. The algorithm is **probabilistic** as it has a chance of returning an incorrect solution. Randomised algorithms present a facinating idea that we can use randomness to find efficient *good-enough* solutions to difficult problems.

## Problem 2: Ford-Fulkerson Algorithm

### Problem Statement
Prove that finding the maximum flow in a network is equivalent to finding the minimum cut of a network.
The Ford-Fulkerson algorithm is a greedy algorithm that can be used to find the maximum flow in a network. 
The maximum flow is the maximum amount of flow that can be pushed through the network from the source to the sink.

### Solution

### Key Take aways

###  Idea behind the Ford-Fulkerson Algorithm
Let P be a path from source to sink in a flow network G. We need to satisfy the following conditions:
- For each properly oriented edge (u,v) in P, we have Flow(u,v) < Capacity(u,v)
- For each properly oriented edge (u, v) in P, we have Flow(u,v) > 0

Let delta be the minimum of the differences Capacity(u,v) - Flow(u,v) over all **properly oriented** edges (u,v) in P. 
```
               | Flow(u, v),            if (u, v) is not in P 
Flow*(u, v) =  | Flow(u, v) + delta,    if (u, v) is in P and properly oriented
               | Flow(u, v) - delta,    if (u, v) is in P and improperly oriented
```
Since the edge (u,v) in P is increased by delta, the value of Flow*(u,v) is delta greater than the value of Flow(u,v) before the augmentation.

## Readings and Resources
**Discrete Mathemathics** - Richard Johnsonbaugh
- Chapter 10: Network Models

**Introduction to Algorithms** - Cormen, Leiserson, Rivest & Stein
- Chapter 26: Maximum Flow

**A New Approach to the Minimum Cut Problem** - Karger & Stein 1996

**More randomized algorithms: Karger’s MinCut Algorithm** - Aleks Ignjatovic (School of Computer Science and Engineering University of New South Wales)