# module two tasks

## Task 0: Provide a short overview of what you learned in the module.

- Review the lecture/seminar materials and summarize the key points, particularly focusing on **Dependency Inversion Principle (DIP)** and **Open-Closed Principle (OCP)**.
- Reflect on your interaction with the unit chair/tutors/peers and summarize insights you gained.
- Highlight any additional research you did outside of the module content, be it online or in the library. 
    - **Remember to cite your sources appropriately.**
    - [refactoring guru](https://refactoring.guru/)
    - **Design Principles and Design Patterns by Robert C. Martin**
- If you interacted with ChatGPT, document the prompts you used and summarize the information you obtained.

## Task 1: Re-factor tic-tac-toe code

- First, revisit your original tic-tac-toe code or download the provided code.
- Start the refactoring process by **identifying areas where DIP and OCP can be applied**.
### DIP: Ensure that your modules depend on abstractions and not on concretions.
### OCP: Make your code open for extension, but closed for modification.
- Allow for variable board size. 
    - Make sure your code can **handle different board sizes**, such as 3x3, 5x5, or 9x9.
- **Plan for future extensions** like different algorithms (minimax, reinforcement learning, etc.). 
     - You don't have to implement these now, but make sure your design can accommodate them.
- Implement a simple **framework for easy addition** of multiple algorithms for various complexities.
- Draw a **class diagram** illustrating your design using correct **UML syntax**. 
     - You can include this in your ipynb notebook as a picture.

## Task 2: Check activity 1 to make sure that your use of inheritance is safe

- Review your refactored code and **validate your use of inheritance**. 
- Make sure that it adheres to Liskov's Substitution Principle (LSP). 
     - **LSP** is a concept in object-oriented programming that states that if a program is using a base class, it should be able to use any of its subclasses without the program knowing it.
- Provide a **detailed explanation** of why you opted to use **inheritance over composition (containment).** 
    - Highlight the **benefits and trade-offs**, focusing on your specific use case.