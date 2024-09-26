# 0x09. Island Perimeter

For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

### Concepts Needed:
#### 1. 2D Arrays (Matrices):

* Accessing and iterating over elements in a 2D array.
* Understanding how to navigate through adjacent cells (horizontally and vertically).
#### 2.Conditional Logic:

* Applying conditions to determine whether a cell contributes to the perimeter of the island.
#### 3. Counting Techniques:

* Developing a method to count the edges that contribute to the island’s perimeter.

##### 4. Problem-Solving Strategies

* Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

#### 5. Python Programming:
* Nested loops for iterating over grid cells.
* Conditional statements to check the status of adjacent cells.

### Resources:
* Python Official Documentation:
    Data Structures (list comprehensions, nested list comprehension)
    More on Lists
* GeeksforGeeks Articles:

    Inplace rotate square matrix by 90 degrees
    Transpose a matrix in Single line in Python
* TutorialsPoint:
    Python Lists for basics of list manipulation in Python.
By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.

## Additional Resources
* Mock Technical Interview
## Requirements
### General
* Allowed editors: __vi, vim, emacs__
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using __python3__ (version 3.8.10)
* All your files should end with a new line
* The first line of all your files should be exactly __#!/usr/bin/python3__
* A __README.md__ file, at the root of the folder of the project, is mandatory
* Your code should use the __pycodestyle__ style (version 2.8.0)
* You are not allowed to import any module
* All modules and functions must be documented
* All your files must be executable

# Tasks
### 0. Island Perimeter
Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

grid is a list of list of integers:
* 0 represents water
* 1 represents land
* Each cell is square, with a side length of 1
* Cells are connected horizontally/vertically (not diagonally).
* grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
