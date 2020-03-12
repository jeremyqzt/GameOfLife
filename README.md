# GameOfLife
This program simulates the Conways game of life. The rules are simple:
 - Any cell (Represented by #) with 2/3 nearby cells lives
 - Any space with 3 nearby cell becomes alive 
 - Any cell with less than 2 cells dies
 - Any cell with more than 3 neighbour cell dies

This utilizes the ncurses to simulate and terminates if in 10 turns there are no changes.

This file can run without a configuration file, it will generate a random cell sample.

The configuration file is either space (" "), representing empty or "#", representing a cell. number of columns must match

```
python GoL.py <configuration file>
```
