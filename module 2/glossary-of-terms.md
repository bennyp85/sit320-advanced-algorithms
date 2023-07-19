# Glossary of Terms

**1. Algorithm:**
   * Used for problem-solving and decision-making in a wide range of fields, including computer science and mathematics.
   * Efficient algorithms can perform tasks more quickly and use less computing resources.
   * Examples of algorithms include sorting algorithms like quicksort or mergesort, and search algorithms like binary search or breadth-first search.

**2. Code Refactoring:**
   * Improves code readability and reduces complexity, making the code easier to maintain and extend.
   * Involves making small, incremental changes, like renaming variables for clarity or breaking down a large function into smaller, more manageable functions.
   * While refactoring, it's essential to have a good set of tests to ensure the behavior of the software hasn't changed.

**3. Dependency Inversion Principle (DIP):**
   * It decouples the software modules, which makes them easier to manage and understand.
   * It increases the flexibility of the system by enabling it to be easily changed or extended.
   * It reduces the impact of changes in the details of the low-level modules on the high-level modules.

**4. Open-Closed Principle (OCP):**
   * Encourages developers to extend the behavior of the system using new code, rather than by changing existing code.
   * Helps to avoid issues that can arise from modifying existing code, such as introducing new bugs.
   * Helps in keeping your code easily maintainable, flexible, and robust.

**5. Inheritance:**
   * Helps in code reusability as the child class inherits the properties and functionalities of the parent class.
   * It can be used to represent real-world relationships (like "a cat is a type of animal") in code.
   * Inheritance should be used judiciously as it can make the code harder to understand and maintain if misused. Prefer composition over inheritance where possible.

**6. Composition:**
- Composition allows for creating complex objects by combining simpler objects.
- It promotes code reusability and modularity.
- The composed objects can be easily replaced or modified without affecting the overall structure.

**7. Minimax Algorithm:**
- The minimax algorithm is commonly used in games with two players, such as chess or tic-tac-toe.
- It explores all possible moves and their consequences to determine the best move for the current player.
- The algorithm assumes that both players are playing optimally, trying to minimize their maximum possible loss.

**8. Reinforcement Learning:**
- Reinforcement learning is inspired by how humans learn through trial and error.
- It involves an agent interacting with an environment and learning from the feedback received in the form of rewards or penalties.
- The agent learns to maximize the cumulative reward by adjusting its actions based on past experiences.

**9. Liskov's Substitution Principle (LSP):**
  - **Subtype Requirement:** Subclasses or derived classes should be substitutable for their base or parent class. This means, in simpler terms, that methods or functions that use pointers or references to the base class must be able to use objects of the derived class without knowing it.
  - **Design By Contract:** LSP is closely related to the concept of "Design by Contract" established by Bertrand Meyer. This involves setting preconditions, postconditions, and invariants for classes and their functions, and each of these should hold true even when a derived class is substituted for the base class.
  - **Impact on Inheritance:** The principle restricts some changes that could be made to the class hierarchy during inheritance. This is mainly about strengthening preconditions or weakening postconditions, which are disallowed, as they could potentially violate the principle.

**10. Class Diagram:**
- A type of static structure diagram in UML.
- Describes the structure of a system by displaying its classes, attributes, and relationships.
- Used to provide a visual representation of the system's design.

**11. UML (Unified Modeling Language):**
- A general-purpose modeling language in software engineering.
- Intended to standardize the visualization of system designs.
- Incorporates various diagram types, including class, sequence, and activity diagrams.

**12. Code Smell:**
- An indication of potential issues or bad practices in code.
- Usually represents deeper problems in the system's design or logic.
- Not a bug, but rather a symptom of potential underlying issues.

**13. Test-Driven Development (TDD):**
- A development approach where tests are written before the code.
- Ensures code meets requirements and functions correctly from the start.
- Allows for immediate feedback and promotes cleaner, more maintainable code.

**14. Red-Green-Refactor:**
- Represents the cycle of TDD.
- Start by writing a failing test (red), then write code to make it pass (green).
- After passing, the code is refactored for improvements or optimization.

**15. 'Make it work, Make it right, Make it fast':**
- A three-phase development approach.
- Initially, focus on making the code functional (work).
- Then, improve code quality and readability (right).
- Lastly, optimize for performance (fast).


**16. Module:** In the context of programming, a module is a software component or part of a program that integrates with other components to run a whole system.

**17. Unit Testing:** A level of software testing where individual units or components of a software are tested to validate that each performs as designed.

**18. Abstract Class**: A class that cannot be instantiated and is used to define common characteristics for subclasses.

**19. Stub:** A piece of code used to stand in for some other programming functionality. Stubs may simulate the behavior of existing code or stand in for code yet to be developed.

**20. Tic-Tac-Toe:** A simple game played on a grid where the goal is to get three of your marks (either X or O) in a row, either horizontally, vertically, or diagonally.

**21. Interface:** A programming structure that allows the computer to enforce certain properties on an object (class).

**22. Software Rigitiy:** A software system is rigid if it is difficult to change. This is usually because changing one part of the system requires making changes to many other parts.

**23. Software Fragility:** A software system is fragile if making a change to one part of the system breaks other parts of the system.

**24. Software Immobility:** A software system is immobile if it is difficult to reuse parts of it in other systems.

**25. Software Viscosity:** A software system has high viscosity if it is difficult to make changes to it without breaking it.