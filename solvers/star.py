#!/usr/bin/env python3

from puzzle4 import TOP, LEFT, RIGHT, BOTTOM, bruteforce, humanize

CONSTRAINTS = {
    0: [             (1, RIGHT) ],
    1: [ (0, LEFT ), (2, RIGHT) ],
    2: [ (1, LEFT ), (3, RIGHT), (6, TOP), (7, BOTTOM) ],
    3: [ (2, LEFT ), (4, RIGHT) ],
    4: [ (3, LEFT ), (5, RIGHT) ],

    5: [ (6, BOTTOM) ],
    6: [ (5, TOP ), (2, BOTTOM) ],

    7: [ (2, TOP ), (8, BOTTOM) ],
    8: [ (7, TOP ),            ],
}

solutions = bruteforce(9, CONSTRAINTS)
print("First solution:", humanize(solutions[0]))
print("Number of solutions:", len(solutions))

# for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
#     print(id, ":", humanize(solution))

