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
