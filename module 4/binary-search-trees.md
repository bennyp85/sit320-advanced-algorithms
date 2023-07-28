## Binary Search Trees (BST)

A Binary Search Tree (BST) is a binary tree data structure that has the following properties:

### Key Properties:

1. **Node Structure**: Each node has a key (and possibly an associated value), and two distinguished sub-trees, commonly denoted as left and right.
2. **Left Sub-tree**: All the keys in a node's left sub-tree are less than the node's key.
3. **Right Sub-tree**: All the keys in a node's right sub-tree are greater than the node's key.
4. **Distinct Keys**: No two nodes in the tree have the same key (assuming simple BST).

### Main Operations:

1. **Search**: Locates a node with a given key in the tree.
2. **Insertion**: Adds a new node with a specified key to the tree.
3. **Deletion**: Removes a node with a specified key from the tree.
4. **Traversal**: Processes all nodes of the tree in a specific order, e.g., in-order, pre-order, or post-order.

### Balancing:

A BST is said to be balanced when the depth of two subtrees of every node never differs by more than 1. However, in real-world scenarios, without any balancing mechanisms, BSTs can become skewed.

**Definition**: What is the balance factor of a node in a BST?

**Calculation**: How do you calculate the balance factor of a node in a BST?

**Imbalance Indication**: If a node in a BST has a balance factor of 2 or -2, what does that indicate about the tree's balance?

**Updates**: When inserting or deleting a node in a BST, how would you update the balance factor for affected nodes?

**Re-balancing**: After determining that a BST is imbalanced due to a balance factor violation, what methods can be used to restore balance to the tree?

**Difference**: How is the balance factor different from simply measuring the height of the left and right subtrees?

**Efficiency**: Why is it efficient to maintain and use balance factors when ensuring the tree remains balanced, as compared to recalculating subtree heights every time?

**AVL Trees**: How do AVL trees utilize the concept of balance factor to ensure the tree remains balanced?

**Rotation Types**: If a node in a BST has a negative balance factor and its right child has a positive balance factor, which type of rotation or rotations would likely be necessary to restore balance?

**Importance**: Why is adding a balance factor and maintaining it crucial for the performance of a BST?

### Types of BSTs:

1. **Balanced BSTs**: Trees like AVL or Red-Black Trees ensure that the tree remains approximately balanced, optimizing search times.
2. **Splay Trees**: A type of self-adjusting binary search tree, where recently accessed elements are quick to access again.
3. **Treaps**: A form of binary search tree that uses priorities (randomly assigned) as well as keys to perform rotations.

### Benefits of BST:

1. **Ordered Structure**: This allows for efficient in-order traversal.
2. **Dynamic Data Set**: BSTs can grow and shrink during the runtime, making it ideal for situations where the dataset is dynamic.
3. **Efficient Operations**: Basic operations like search, insertion, and deletion can be efficient, especially in balanced BSTs.

## Binary Search Tree (BST) - Time Complexity

### Search Operation:
- **Best Case**: \(O(\log n)\) 
  - Scenario: The BST is balanced.
  
- **Worst Case**: \(O(n)\) 
  - Scenario: The BST degenerates into a linked list (when elements are inserted in order).

- **Average Case**: \(O(\log n)\) 
  - Scenario: The tree is reasonably well-balanced.

### Insertion Operation:
- **Best Case**: \(O(\log n)\) 
  - Scenario: The BST is balanced.
  
- **Worst Case**: \(O(n)\) 
  - Scenario: The BST becomes skewed (i.e., like a linked list).
  
- **Average Case**: \(O(\log n)\)

### Deletion Operation:
- **Best Case**: \(O(\log n)\) 
  - Scenario: The BST is balanced. Finding the node is \(O(\log n)\), and if it's a node with one or no child, deletion is constant time. For a node with two children, finding the in-order predecessor (or successor) is \(O(\log n)\).
  
- **Worst Case**: \(O(n)\) 
  - Scenario: In a skewed BST.
  
- **Average Case**: \(O(\log n)\)

**Note**: The time complexities can be consistently maintained as \(O(\log n)\) if mechanisms are used to keep the BST balanced, such as in AVL Trees or Red-Black Trees.


### Drawbacks:

1. **Skewed Trees**: Without balancing, BSTs can become skewed, leading to operations becoming inefficient.
2. **Balancing Overhead**: Trees that self-balance (like AVL or Red-Black Trees) can have overheads in maintaining the balance.

### Conclusion:

Binary Search Trees provide a versatile data structure that supports ordered operations. While they offer many advantages, care must be taken (especially in the case of simple BSTs) to ensure they remain efficient in real-world applications by preventing them from becoming too skewed or unbalanced.

