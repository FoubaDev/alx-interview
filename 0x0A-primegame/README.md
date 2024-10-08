# 0x0A. Prime Game

For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.



### Concepts Needed:
#### 1. Prime Numbers:

* Understanding what prime numbers are.
* Efficient algorithms for identifying prime numbers within a range.
#### 2.Sieve of Eratosthenes:

* An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.
#### 3. Game Theory:

* Basic principles of competitive games where players take turns and the concept of optimal play.
* Understanding win conditions and strategies that lead to a win or loss.

##### 4. Dynamic Programming/Memoization:

* Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.

#### 5. Python Programming:
* Loops and conditional statements for implementing game logic and algorithms.
* Arrays and lists for storing the integers and tracking removed numbers.


### Resources:
* Prime Numbers and Sieve of Eratosthenes:
    A step-by-step guide to implementing the sieve algorithm in Python.
* Game Theory Basics:
A simple explanation of game theory and strategic decision-making.
    
* Dynamic Programming:
   An introduction to dynamic programming with Python examples.
* Python Official Documentation:
Managing lists in Python, useful for tracking the game state.

## Additional Resources

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
### 0. Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

* Prototype: def isWinner(x, nums)
* where x is the number of rounds and nums is an array of n
* Return: name of the player that won the most rounds
* If the winner cannot be determined, return None
* You can assume n and x will not be larger than 10000
* You cannot import any packages in this task
__Example:__
* x = 3, nums = [4, 5, 1]
__First round: 4__

* Maria picks 2 and removes 2, 4, leaving 1, 3
* Ben picks 3 and removes 3, leaving 1
* Ben wins because there are no prime numbers left for Maria to choose
__Second round: 5__

* Maria picks 2 and removes 2, 4, leaving 1, 3, 5
* Ben picks 3 and removes 3, leaving 1, 5
* Maria picks 5 and removes 5, leaving 1
* Maria wins because there are no prime numbers left for Ben to choose
__Third round: 1__

Ben wins because there are no prime numbers for Maria to choose
__Result: Ben has the most wins__