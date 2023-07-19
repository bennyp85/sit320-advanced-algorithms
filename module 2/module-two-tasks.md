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

---


- [ ] Working TicTacToe game.
- [ ] Ability to choose board dimensions.
- [ ] Ability to select an algorithm to play against.
- [ ] Supported configurations: human/human, human/computer, computer/computer.
- [ ] Open-Closed Principle (OCP) adhered to.
- [ ] Dependency Inversion Principle (DIP) adhered to.
- [ ] Liskov Substitution Principle (LSP) adhered to.
- [ ] UML Diagram.
- [ ] Unit Testing.
- [ ] Short video presentation.
- [ ] Summary of learning.

Considering the checklist, here are the next steps:

#### UML Diagram:
   - Before you start, list down all the classes, interfaces, and their relationships. Also, consider attributes and operations for each class.
   - Use a UML tool or software to create the diagram. Tools like [draw.io](https://www.draw.io/), Lucidchart, or even Microsoft Visio can be used.
   - Make sure to follow the correct UML syntax and symbols for classes, interfaces, relationships, etc.

#### Short Video Presentation:
   - Start by writing down key points you want to cover.
   - Introduce the problem, your approach, and the main features of your implementation.
   - Discuss the principles you've applied and give brief examples from your code.
   - A screen recording software like OBS Studio or Screencast-O-Matic can be handy. Show your code running, demonstrate its features, and walk through a few important code segments.

#### Summary of Learning:
   - Reflect on the entire process: the initial understanding of the task, challenges faced, what you've learned about design principles, and any feedback or insights from peers/tutors.
   - Mention how the interaction with tools (like ChatGPT) aided in your understanding.
   - Highlight any 'aha' moments or points of confusion that you managed to clarify. **push functions up**

Finally, do a quick self-review:
   - Run the game in all configurations to ensure everything works smoothly.
   - Check if the game handles edge cases or unexpected inputs gracefully.
   - Ensure that your code is well-documented, especially in parts where design principles are applied.
