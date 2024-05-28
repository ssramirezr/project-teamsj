# Project - Formal Languages And Compilers

**Group members:** Santiago Manco Maya and Juan José Gómez Vélez

The assignment was to implement algorithms to compute the First and Follow sets of non-terminal symbols of a given context free grammar.

## Versions and Programming Language

**Version of the OS used:** Windows 11.

**Programming Language:** Python 3.10.12

**Tools:** IDE Visual Studio Code

## Instructions for running the implementation

**1.** Download the project.py file.

**2.** Use the cd command in the console to access the folder where the file project.py is located.

**3.** Run the project.py file by using the next command:
```
py project.py
```

**4.** The program will print the First and Follow sets of each non-terminal symbol of the given grammar
```
3
2
S AS A
A a
First(S) = {a}
First(A) = {a}
Follow(S) = {$}
Follow(A) = {a, $}
3
S AB
A aA a
B bBc bc
First(S) = {a}
First(A) = {a}
First(B) = {b}
Follow(S) = {$}
Follow(A) = {b}
Follow(B) = {c, $}
2
S A
A A b
First(S) = {b}
First(A) = {b}
Follow(S) = {$}
Follow(A) = {$}
```

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kw1YU2tQ)
