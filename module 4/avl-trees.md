## AVL Tree

An AVL tree, named after its inventors Adelson-Velsky and Landis, is a self-balancing binary search tree. The distinguishing feature of an AVL tree is its height-balance property.

## Height-Balance Property

In an AVL tree, for every node, the difference between the heights of its left and right subtrees (often referred to as the "balance factor") is never more than one. This balance factor can have one of the following values:

- **-1**: The right subtree is taller by one level.
- **0**: Both subtrees have the same height.
- **1**: The left subtree is taller by one level.

If, due to an operation like insertion or deletion, the balance factor for any node in the tree falls outside this range (i.e., becomes less than -1 or greater than 1), the tree becomes unbalanced. In such cases, rebalancing rotations are performed to restore the height balance.

## Rotations to Maintain Balance

To rectify imbalance, AVL trees employ four types of rotations:

## Tree Rotations

When maintaining the balance of AVL trees (or other balanced trees), rotations are essential. Depending on the imbalance's location, there are different rotations to apply. Here's a breakdown:

### 1. Single Right Rotation (LL Rotation)
- **When to Apply**: Applied when a node is left-heavy and its left child is also left-heavy.
- **Operation**: The imbalanced node is rotated to the right.

### 2. Single Left Rotation (RR Rotation)
- **When to Apply**: Applied when a node is right-heavy and its right child is also right-heavy.
- **Operation**: The imbalanced node is rotated to the left.

### 3. Left-Right Rotation (LR Rotation)
- **When to Apply**: Applied when a node is left-heavy but its left child is right-heavy.
- **Operation**: First, a left rotation is applied to the left child, followed by a right rotation on the imbalanced node.

### 4. Right-Left Rotation (RL Rotation)
- **When to Apply**: Applied when a node is right-heavy but its right child is left-heavy.
- **Operation**: First, a right rotation is applied to the right child, followed by a left rotation on the imbalanced node.

By correctly applying these rotations, the balance of the tree can be maintained, ensuring optimal performance for tree operations.

## Advantages of Height-Balance

The enforcement of the height-balance property ensures that AVL trees always have logarithmic height relative to the number of nodes (`n`). As a result, all primary operations (insert, delete, and find) are guaranteed to run in O(log n) time. This consistent performance is a stark contrast to regular binary search trees, which can degenerate into linked lists, making operations run in O(n) time in the worst case.

## Conclusion

The height-balance property and the associated rotations to maintain it ensure that AVL trees offer efficient and predictable performance, making them a valuable choice for many applications where balanced search trees are required.
