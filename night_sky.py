#!/usr/bin/env python3

from puzzle3 import BASE, RIGHT, LEFT, bruteforce, humanize

CONSTRAINTS = {
    0: [ (1, BASE) ],
    1: [ (0, BASE) ],

    2: [ (3, BASE) ],
    3: [ (2, BASE) ],

    4: [ (5, BASE) ],
    5: [ (4, BASE) ],

    6: [ (7, BASE) ],
    7: [ (6, BASE) ],
}

solutions = bruteforce(9, CONSTRAINTS)
print("First solution:", humanize(solutions[0]))
print("Number of solutions:", len(solutions))

# for id, solution in enumerate(bruteforce(8, CONSTRAINTS)):
#     print(id, ":", humanize(solution))
