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


**6. Composition:** A design principle in object-oriented programming where a class can have an instance of another class as a field of the class.

**7. Minimax Algorithm:** A decision-making algorithm for minimizing the worst-case potential loss in games with two players.

**8. Reinforcement Learning:** A type of machine learning where an agent learns how to behave in an environment by performing actions and getting rewards or penalties.

**9. Liskov's Substitution Principle (LSP):** LSP is a principle in object-oriented programming that states if a program is using a base class, it should be able to use any of its subclasses without the program knowing it.
  - **Subtype Requirement:** Subclasses or derived classes should be substitutable for their base or parent class. This means, in simpler terms, that methods or functions that use pointers or references to the base class must be able to use objects of the derived class without knowing it.
  - **Design By Contract:** LSP is closely related to the concept of "Design by Contract" established by Bertrand Meyer. This involves setting preconditions, postconditions, and invariants for classes and their functions, and each of these should hold true even when a derived class is substituted for the base class.
  - **Impact on Inheritance:** The principle restricts some changes that could be made to the class hierarchy during inheritance. This is mainly about strengthening preconditions or weakening postconditions, which are disallowed, as they could potentially violate the principle.


**10. Class Diagram:** A type of static structure diagram in UML that describes the structure of a system by showing the system's classes, their attributes, and the relationships among the classes.

**11. UML (Unified Modeling Language):** A general-purpose, developmental, modeling language in the field of software engineering that is intended to provide a standard way to visualize the design of a system.

**12. Code Smell:** A surface indication that usually corresponds to a deeper problem in the system.

**13. Test-Driven Development (TDD):** A software development approach in which a test is written before writing the code. When the test passes, the code is refactored as necessary.

**14. Red-Green-Refactor:** A TDD process where you first write a failing test (red), make it pass in the simplest way possible (green), and then refactor.

**15. 'Make it work, Make it right, Make it fast':** A development approach where you first make the code work, then refactor it for readability and maintainability, and finally optimize it for performance.

**16. Module:** In the context of programming, a module is a software component or part of a program that integrates with other components to run a whole system.

**17. Unit Testing:** A level of software testing where individual units or components of a software are tested to validate that each performs as designed.

**18. Abstract Class**: A class that cannot be instantiated and is used to define common characteristics for subclasses.

**19. Stub:** A piece of code used to stand in for some other programming functionality. Stubs may simulate the behavior of existing code or stand in for code yet to be developed.

**20. Tic-Tac-Toe:** A simple game played on a grid where the goal is to get three of your marks (either X or O) in a row, either horizontally, vertically, or diagonally.

**21. Interface:** A programming structure that allows the computer to enforce certain properties on an object (class).