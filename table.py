#!/usr/bin/env python3

from puzzle4 import TOP, LEFT, RIGHT, BOTTOM, bruteforce, humanize

CONSTRAINTS = {
    0: [             (1, RIGHT) ],
    1: [ (0, LEFT ), (2, RIGHT), (7, BOTTOM) ],
    2: [ (1, LEFT ), (3, RIGHT) ],
    3: [ (2, LEFT ), (4, RIGHT) ],
    4: [ (3, LEFT ), (5, RIGHT) ],
    5: [ (4, LEFT ), (6, RIGHT), (8, BOTTOM) ],
    6: [ (5, LEFT ), (7, RIGHT) ],

    7: [ (1, TOP) ],
    8: [ (5, TOP) ],
}

solutions = bruteforce(9, CONSTRAINTS)
print("First solution:", humanize(solutions[0]))
print("Number of solutions:", len(solutions))

# for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
#     print(id, ":", humanize(solution))

