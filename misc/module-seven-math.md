# Mathematical Concepts in Dynamic Programming
## School of Information Technology, Deakin University
### SIT320 — Advanced Algorithms
### Module Seven — Dynamic Programming

## Table of Contents
1. [Introduction](#introduction)
2. [Running Up Stairs](#running-up-stairs)
3. [Longest Common Subsequence (LCS)](#longest-common-subsequence-lcs)
4. [0/1 Knapsack Problem](#01-knapsack-problem)
5. [Conclusion](#conclusion)

## Introduction
Dynamic Programming (DP) is a method used in computer science to solve problems by breaking them into overlapping subproblems. The mathematical foundations of DP involve concepts of optimization, recurrence relations, and combinatorial analysis.

## Running Up Stairs
### Problem Statement
Given a staircase with \( n \) steps, and the ability to hop 1, 2, or 3 steps at a time, find the number of ways to reach the top.
### Mathematical Formulation
The problem can be defined using the recurrence relation:
- \( F(n) = F(n-1) + F(n-2) + F(n-3) \)
- With base cases: \( F(0) = 1, F(1) = 1, F(2) = 2 \)
### Complexity
- Time Complexity: \( O(n) \)
- Space Complexity: \( O(n) \)

## Longest Common Subsequence (LCS)
### Problem Statement
Given two sequences \( X \) and \( Y \), find the length of the longest subsequence common to both.
### Mathematical Formulation
The problem can be solved using a 2D matrix \( C \) where:
- \( C[i][j] = 0 \) if \( i = 0 \) or \( j = 0 \)
- \( C[i][j] = C[i-1][j-1] + 1 \) if \( X[i] = Y[j] \)
- \( C[i][j] = \max(C[i-1][j], C[i][j-1]) \) if \( X[i] \neq Y[j] \)
### Complexity
- Time Complexity: \( O(m \cdot n) \)
- Space Complexity: \( O(m \cdot n) \)

## 0/1 Knapsack Problem
### Problem Statement
Given weights and values of \( n \) items, put these items in a knapsack of capacity \( W \) to get the maximum total value.
### Mathematical Formulation
The problem can be defined using a 2D matrix \( K \):
- \( K[i][w] = 0 \) if \( i = 0 \) or \( w = 0 \)
- \( K[i][w] = K[i-1][w] \) if \( wt[i-1] > w \)
- \( K[i][w] = \max(val[i-1] + K[i-1][w - wt[i-1]], K[i-1][w]) \) if \( wt[i-1] \leq w \)
### Complexity
- Time Complexity: \( O(n \cdot W) \)
- Space Complexity: \( O(n \cdot W) \)

## Conclusion
Dynamic Programming provides an elegant approach to solve complex problems by breaking them down into smaller, manageable subproblems. The mathematical principles underlying DP are central to understanding its efficiency and versatility.

