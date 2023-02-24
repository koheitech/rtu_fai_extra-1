# README
This is the program that solves the [Bridge and torch problem](https://en.wikipedia.org/wiki/Bridge_and_torch_problem) using recursion

## Problem description
**Create a state space graph for the problem given below:**

Three travelers (let's call them A, B and C) met at night at a narrow bridge (let's call the meeting point P1). 
They all have to cross the bridge and get to the other side (let's call it P2). Nothing can be seen around. 
At the bridge, the travelers have access to one torch which, once lit, burns for 12 minutes. 
It must be used when crossing the bridge. E
ach of the travelers is able to cross the bridge in a certain time: A - 1 minute, B - 3 minutes, C - 5 minutes. 
Thus, for all travelers to cross safely from P1 to P2, the following conditions must be met:
- The bridge can only be crossed from P1 to P2 by two travelers carrying the torch
- The bridge is crossed alone in the opposite direction from P2 to P1, carrying the torch
- When two travelers cross the bridge, the time of the slowest traveler is taken as the time of crossing the bridge
- The torch burning time decreases according to the bridge crossing time
- If the torch burning time is less than the bridge crossing time, the bridge may not be crosse

## Information
- language: python 3.1.1

## How to run
- download the code
- run the code using following command
    ```bash
    python3 app.py
    ```