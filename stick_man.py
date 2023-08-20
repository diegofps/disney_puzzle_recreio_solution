#!/usr/bin/env python3

from puzzle4 import TOP, LEFT, RIGHT, BOTTOM, bruteforce, humanize

CONSTRAINTS = {
    0: [ (2, BOTTOM )                        ],
    1: [ (2, RIGHT  )                        ],
    2: [ (0, TOP    ), (1, LEFT), (3, RIGHT), (4, BOTTOM) ],
    3: [ (2, LEFT   )                        ],
    4: [ (2, TOP), (6, BOTTOM) ],
    5: [ (6, RIGHT) ],
    6: [ (5, LEFT), (7, RIGHT) ],
    7: [ (6, LEFT) ],
}

solutions = bruteforce(9, CONSTRAINTS)
print("First solution:", humanize(solutions[0]))
print("Number of solutions:", len(solutions))

# for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
#     print(id, ":", humanize(solution))

