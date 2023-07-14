# thoughts on design patterns

## design patterns
- patterns are not specific pieces of code but rather general concepts that can be applied to different situations
- patterns are not algorithms but rather templates for solving problems
- an analogy for an algorithms is a recipe, whereas a pattern is a cooking technique
- patterns consist of:
    - intent
    - motivation
    - structure
    - example code

## history of patterns
- christopher alexander
    - architect
    - wrote a book called "a pattern language"
    - patterns are a way of describing good design practices
- erich gamma, richard helm, ralph johnson, john vlissides
    - wrote a book called "design patterns: elements of reusable object-oriented software"
    - the book is commonly referred to as the "gang of four" book
    - the book describes 23 patterns
    - the book is considered the bible of design patterns

## why learn patterns
- tried and tested solutions to common problems
- common vocabulary for developers

## criteria for patterns
- kludges for weak programming languages
- can be inefficient soltions
- unjustified use of patterns

## classification of patterns
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



