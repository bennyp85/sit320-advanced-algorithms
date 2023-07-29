# Plan for SIT320 — Advanced Algorithms: Trees

## 1. Module Overview
- **Sources for Overview**:
    - Seminar lectures and notes
    - Module content on Cloud Deakin
    - Interactions with Unit Chair, Tutors, and Peers
    - Independent research (library, internet, etc.)
    - Interactions with chatGPT (remember to note down the prompts used)

## 2. Modify the BST for Balance
- **Steps**:
    1. Update the node structure to include a new field for balance.
    2. Adjust the insert operation to update the balance.
    3. Adjust the delete operation to update the balance.
    4. Implement a function to check the balance of the entire tree.
        - Should return `True` if balanced, `False` otherwise.

## 3. Find First Common Ancestor
- **Steps**:
    1. Create a function that takes two nodes and a BST as input.
    2. Search for the nodes in the BST.
    3. Determine the first common ancestor of the nodes.
    4. Return the common ancestor node.

## 4. Tree Rotations
- **Steps**:
    1. Define a function to perform the four types of rotations:
        - Left rotation
        - Right rotation
        - Left-Right rotation
        - Right-Left rotation
    2. The function should take in the tree and a specific node for rotation.
    3. Return the tree with the applied rotation.

## 5. Testing
- Implement various test cases for:
    - Checking the balance of the BST
    - Finding the first common ancestor
    - All four rotation types

## 6. Code Implementation
- Based on your comfort with Python, decide whether to start with the provided code or implement from scratch.
- Add the code at the end of the provided `ipynb` file.

## 7. Review and Submission
- Complete the lesson review.
- Submit for tutor review and address any feedback or follow-up questions.

## 8. Finalize
- Make any necessary revisions based on tutor feedback.
- Ensure that all parts of the task are completed and tested.

## Strategy Pattern

**Definition**:
The Strategy Pattern defines a set of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from the clients that use it.

**Components**:
1. **Strategy**: This is an interface common to all supported algorithms. It declares a method for executing an algorithm.
2. **ConcreteStrategy**: This class implements the `Strategy` interface, providing the actual implementation for the algorithm.
3. **Context**: Uses a `Strategy` to execute the algorithm. It contains a reference to a Strategy object and may define an interface that lets Strategy access its data.

**Advantages**:
- Enables a client to choose from a family of algorithms without altering the code that uses the algorithm.
- Encapsulates the algorithm from the code that uses it.
- Promotes adding new algorithms or changing existing algorithms without altering existing code.

**Use in SIT320 — Advanced Algorithms: Trees**:
- Different methods to balance trees (like AVL and Red-Black Trees) can be strategies.
- Various rotations (left, right, left-right, right-left) are strategies to balance individual nodes.
- The strategy pattern can be used to implement these algorithms and rotations in a way that is interchangeable and independent from the client code.
