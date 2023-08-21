#!/usr/bin/env python3

from puzzle4 import TOP, LEFT, RIGHT, BOTTOM, bruteforce, humanize

CONSTRAINTS = {
    0: [(1, RIGHT) ],
    1: [(0, LEFT ) ],

    2: [ (3, BOTTOM) ],
    3: [ (2, TOP  ), (4, RIGHT) ],
    4: [ (3, LEFT ), (5, RIGHT) ],
    5: [ (4, LEFT ), (6, RIGHT) ],
    6: [ (5, LEFT ), (7, RIGHT) ],
    7: [ (6, LEFT ), (8, TOP) ],
    8: [ (7, BOTTOM ) ],
}

solutions = bruteforce(9, CONSTRAINTS)
print("First solution:", humanize(solutions[0]))
print("Number of solutions:", len(solutions))

# for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
#     print(id, ":", humanize(solution))

