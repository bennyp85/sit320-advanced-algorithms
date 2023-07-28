## Red-Black Trees

A Red-Black Tree (RBT) is a type of self-balancing binary search tree. Each node in the tree has an extra attribute: color, which can be either red or black. The Red-Black Tree satisfies specific properties that ensure it remains approximately balanced, resulting in O(log n) time for major operations like insertions, deletions, and lookups.

### Key Properties:

1. **Node Color**: Every node is colored, either red or black.
2. **Root Property**: The root node is always black.
3. **Red Node Property**: Red nodes can't have red children (i.e., no two consecutive red nodes are allowed).
4. **Black Height Property**: For each node, any path from this node to any of its descendant leaves has the same black height (number of black nodes).
5. **New Insertions**: Newly inserted nodes are always red initially.

### Balancing the Tree:

When nodes are inserted or deleted, the above properties might be violated. To restore the properties, the tree undergoes a series of transformations, such as color changes and rotations (left or right).

### Comparison with AVL Trees:

- **Balancing**: AVL trees are more rigidly balanced, while RBTs provide a more relaxed balancing, ensuring that the tree remains approximately balanced.
- **Operations**: AVL trees may require more rotations during insertion and deletion, while RBTs might need fewer adjustments.
- **Usage**: RBTs are used in many real-world systems like the Linux kernel and some databases because they offer consistent performance and simpler restructuring than AVL trees.

### Conclusion:

Red-Black Trees are a powerful tool when a balanced binary search tree is required. They ensure efficient performance for primary tree operations without the stricter balancing criteria of AVL trees.
