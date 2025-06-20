# Accelerating Compilation – Parallel Lexical Analysis in Modern Compilers
---

## Description
This project explores how we can speed up one of the slowest parts of compiling code: the lexical analysis phase by doing it in parallel. Using Python, we simulate splitting source code into pieces and processing them at the same time to tokenize faster. The idea is based on by LLVM’s compiler design and aims to show how multi-threading could make compiling big programs quicker.

---

## Why does it matter?  
- Compiling big projects can be slow and frustrating.  
- By parallelizing lexical analysis, we can cut down that wait time.  
- Faster compiles mean better productivity and happier developers.  
- This lays groundwork for future real-world compilers that use parallelism.

---

## Functionalities:  

We built a mini-compiler pipeline that includes:

- **Lexical Analysis:** Tokenizes code using a simple parallel simulation.  
- **Syntax Analysis:** Creates an Abstract Syntax Tree (AST) from tokens.  
- **Intermediate Representation (IR):** Converts AST into a set of simple instructions.  
- **Optimization:** Uses constant folding to do math at compile time and simplify code.  
- **Code Generation:** Outputs pseudo-assembly instructions to mimic machine code.  
- **Register Allocation Simulation:** Shows how variables might be assigned to CPU registers.

---

## What did we learn?  

- Parallel tokenization can be up to 5x faster (even with simple simulations).  
- AST depth helps us understand expression complexity and operator precedence.  
- Optimizing IR reduces the number of instructions, making execution more efficient.  
- Register allocation helps manage CPU resources smartly during compilation.

---

## What’s missing or limited?  

- Only handles basic math with numbers — no variables or control flow yet.  
- Parallelism is simulated, not real multi-threading (that’s coming!).  
- Minimal error checking for now.  
- The generated code is not tied to any real CPU architecture.

---

## What’s next?  

- Implement actual multi-threaded lexical analysis to test real speed-ups.  
- Add support for variables, loops, and more complex syntax.  
- Include semantic checks like type validation and scope handling.  
- Connect to LLVM or other backends to generate real machine code.  
- Add smarter optimizations like dead code removal and constant propagation.  
- Improve register allocation with graph-based algorithms.  
- Build performance tools to measure speed and memory improvements.

---

## Tools and Technologies Used

- Python (3.8 to 3.12 recommended) for all code and simulations.  
- Only built-in Python libraries — no need for extra installs.  
- Inspired by LLVM compiler architecture (for ideas and design).

---

## Setup Instructions :  
1. Make sure you have Python installed with newer versions.
   - python --version

2. Run the application with:
   - python simulation_runner.py

   - **You can quickly test by just running the scripts from the terminal or IDE. You do not need GUI or any complex setups.**

## License
This project is licensed under the MIT License. 
