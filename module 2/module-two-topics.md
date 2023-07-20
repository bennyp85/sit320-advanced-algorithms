# module two

## Glossary of Terms

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

**16. Module:**
- A self-contained component that can be reused in various contexts within a software system.
- Can contain functions, classes, or variables, and can group related code for easier management and understanding.
- Helps in organizing code, reducing namespace collisions, and promoting code reuse.

**17. Unit Testing:**
- Focuses on verifying the correctness of individual units of source code, usually the smallest part of a software system.
- Is typically automated and run frequently to catch regressions early.
- Can be written before or after the actual code, though Test-Driven Development (TDD) promotes writing tests before code.

**18. Abstract Class:**
- A class that serves as a blueprint for other classes but cannot be instantiated directly.
- Used to define common methods and properties that can be inherited by subclasses.
- Can contain both concrete methods (with implementation) and abstract methods (without implementation).

**19. Stub:**
- Used to simulate the behaviors of real objects in a controlled way, primarily in unit testing.
- Simplified implementations of interfaces or abstract classes.
- Can be manually written or generated using mocking frameworks.

**20. Tic-Tac-Toe:**
- A two-player game with a 3x3 grid, where players take turns placing their mark (X or O).
- The player who gets three of their marks in a line (horizontally, vertically, or diagonally) first wins.
- Often used as a beginner project in programming due to its simplicity.

**21. Interface:**
- Defines a contract or set of methods that a class must implement.
- Promotes the design principle of "programming to an interface, not an implementation."
- Used to achieve polymorphism and decoupling in object-oriented programming.

**22. Software Rigidity:**
- Indicates difficulty in making modifications without extensive changes.
- Often a result of tight coupling between modules or components.
- Can increase the time and cost of maintaining or extending software.

**23. Software Fragility:**
- Changes to one part of the system unexpectedly break other parts.
- Often a consequence of hidden dependencies or lack of adequate testing.
- Increases the risk of introducing defects when making changes.

**24. Software Immobility:**
- Components of the software are difficult to reuse in other projects.
- Often due to tight coupling or lack of modular design.
- Reduces the benefits of code reuse and increases development effort.

**25. Software Viscosity:**
- Represents the resistance to change within a software system.
- Changes might be done in a manner that's easier but violates design principles.
- Results in accumulating technical debt over time.

**Dependency Injection:**
- A technique to achieve Inversion of Control, where dependencies are "injected" into a component rather than created by the component itself.
- Promotes decoupling, making systems more modular and easier to test.
- Commonly implemented using frameworks or containers in many programming languages.

**Polymorphism:**
- A foundational concept in OOP, allowing objects of different classes to be treated as objects of a common super class.
- Supports the ability of different classes to respond to the same method call in a way specific to their individual types.
- Enhances flexibility and reusability in software design.
---
## Inheritance vs. Composition in Tic-Tac-Toe

1. **Inheritance Basis**:
   - Did you have a "is-a" relationship between classes? Can you give an example from your code where one class "is a type of" another class?
   - Were there shared attributes or methods among various classes that made it easier to use a base class and then derive subclasses?

2. **Code Reusability**:
   - By using inheritance, did you find it easier to reuse code from the parent class in multiple child classes? 
   - Can you think of methods or attributes that were inherited and then possibly overridden or extended in subclasses?

3. **Flexibility**:
   - In what ways did inheritance provide flexibility to your design? 
   - Could you easily add new features or make changes to derived classes without modifying the base class?

4. **Composition Considerations**:
   - Why didn't you choose composition for your design? Were there specific challenges or complexities that discouraged its use?
   - How would your design look if you opted for composition over inheritance? Would it be more modular or more fragmented?

5. **Trade-offs**:
   - What are the potential downsides or challenges you faced or might face using inheritance in your Tic-Tac-Toe game design?
   - Did you encounter or foresee issues related to tight coupling, where changes in the base class might inadvertently affect the derived classes?

6. **Extensibility**:
   - Thinking about future developments, do you think using inheritance will make it easier or harder to extend your game, say by adding new features or algorithms?

7. **Readability and Maintenance**:
   - How does inheritance impact the readability of your code?
   - Does inheritance make it easier or more challenging for another developer to pick up and understand your codebase?
---
## thoughts on design patterns

### design patterns
- patterns are not specific pieces of code but rather general concepts that can be applied to different situations
- patterns are not algorithms but rather templates for solving problems
- an analogy for an algorithms is a recipe, whereas a pattern is a cooking technique
- patterns consist of:
    - intent
    - motivation
    - structure
    - example code

### history of patterns
- christopher alexander
    - architect
    - wrote a book called "a pattern language"
    - patterns are a way of describing good design practices
- erich gamma, richard helm, ralph johnson, john vlissides
    - wrote a book called "design patterns: elements of reusable object-oriented software"
    - the book is commonly referred to as the "gang of four" book
    - the book describes 23 patterns
    - the book is considered the bible of design patterns

### why learn patterns
- tried and tested solutions to common problems
- common vocabulary for developers

### criteria for patterns
- kludges for weak programming languages
- can be inefficient soltions
- unjustified use of patterns

### classification of patterns
- creational
    - abstract the instantiation process
    - encapsulate knowledge about which concrete classes the system uses
    - hide how instances of these classes are created and put together
- structural
    - describe how classes and objects can be combined to form larger structures
    - focus on the composition of classes and objects
    - emphasize the design of a system
- behavioral
    - describe how classes and objects interact with each other
    - focus on how objects distribute work
    - emphasize the communication between objects


# design patterns pdf - robert c. martin

The document discusses **software architecture and design patterns**, focusing on the principles and patterns that help maintain the dependency architecture of an application.

It highlights the problem of **software rot**, where the design of software applications begins to degrade over time due to changes and modifications, leading to symptoms like rigidity, fragility, immobility, and viscosity.

The document emphasizes the importance of **dependency management** in software design, suggesting the creation of **dependency firewalls** to prevent the propagation of dependencies.

It introduces the **Principles of Object Oriented Class Design**, starting with the **Open Closed Principle (OCP)**, which states that a module should be open for extension but closed for modification.

The **Liskov Substitution Principle (LSP)** is discussed, which states that subclasses should be substitutable for their base classes. Violations of this principle can lead to issues in software design and maintenance.

The **Dependency Inversion Principle (DIP)** is presented, which advises to depend upon abstractions and not concretions. This principle is the enabling force behind component design, COM, CORBA, EJB, etc.

The document discusses the **Circle/Ellipse dilemma** as an example of the Liskov Substitution Principle, illustrating the potential issues that can arise when the principle is violated.

It explains the concept of **Design by Contract**, where a method declares what must be true before the method is called (precondition) and what the method guarantees will be true once it has completed (postcondition).

The document contrasts the **dependency structures** of procedural and object-oriented architectures, with the latter showing a structure where the majority of dependencies point towards abstractions.

It concludes by discussing the mitigating forces against the Dependency Inversion Principle, acknowledging that while the principle assumes anything concrete is volatile, there are exceptions such as tried and true modules that are concrete but not volatile.
---
## dependency inversion principle

### dependencies
- relationship (assoctions) between various entities
- dependency: when one entity depends on another entity
    - for example in python one package can depend on another package
- safe dependencies: when a change in one entity does not affect the other entity

### stable design
- stable design: when a change in one entity does not affect the other entity
- stable design is achieved by using abstractions

### abstraction
- abstraction: a simplified representation of a complex entity
- abstraction is achieved by using interfaces
- abstract things change less frequently than concrete things

### procedural programming vs object oriented programming
- procedural programming: code is organized around procedures or functions
- object oriented programming: code is organized around objects

## open closed principle

### open for extension, closed for modification
- open for extension: the behavior of a module can be extended
    - example: adding a new algorithm to a module
- closed for modification: the source code of a module is not modified
    - example: adding a new algorithm to a module without modifying the source code of the module
- the aim is to write code that does not have to be modified when new functionality is added