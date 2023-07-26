# Module Three Lesson Review

## Task 0: Overview of Learning
- [GitHub Repo Link](https://github.com/bennyp85/sit320-advanced-algorithms/tree/master/module%203)
- [ChatGPT Link]()
- [YouTube Video Line]()

- **Design patterns** are a set of solutions to common problems in software design. They are reusable and can be applied to different problems in different contexts.
- **Factory patterns** are a type of design pattern that are used to create objects without exposing the creation logic to the client and refer to newly created objects using a common interface.
- In the TicTacToe code this was acheived by creating a **TicTacToeFactory**. This was responsible for creating the Board, Game Logic, Algorithm, and Player objects.
- In this moduile we used the **abstract factory pattern** to create a framework for multiple games. The framework is designed to be expandable for additional games and algorithms in the future.
- This design pattern provides a **Framwork** for further expansion. 
- **Singletons** are a type of design pattern that restricts the instantiation of a class to one object.
- They are useful for situations where you need to control access to a shared resource.
- This is acheived by the use of a private constructor and a static method to return the instance of the object.
- **Facade patterns** are a type of design pattern that provides a simple interface to a complex system.
- I haven't really come accrross this pattern in my work. But it makes sense that it would be implented for complex libraries and frameworks.

**Aha Moments!**
- Seeing the **observer pattern** in action was a great way to understand how it works.
- The Pizza example really helped me understand the **Factory Pattern**.
- The practical uses of the **Singleton Pattern** were very interesting. Examples such as the **Logger** and **Database Connection** were very useful.
- I have been actively analysing other peoples code on GitHub and looking to see if I can recognise any design patterns. 
- This will take time and practice to get good at. But I am starting to see some patterns emerge.

## Task 1: Design Pattern for Multiple Games
- [Abstract Factory UML Class Diagram]
- [Abstract Factory GitHub Repo Link](https://github.com/bennyp85/sit320-advanced-algorithms/blob/master/module%203/tic-tac-toe.ipynb)
- The **UML Class Diagram** created for thi module is an example of the **abstract factory pattern**. 
- An **AbstractGameFactory** class is used to create **gameFactory** objects.
- The concrete **TicTacToeFactory** class is used to create the various game objects.

## Task 2: Understanding of Observer Pattern

## Readings
- [Gang of Four Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns) - Wikipedia **I own this book and have not really understood until now. Practical application was key.**