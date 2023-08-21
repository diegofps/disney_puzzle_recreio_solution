#!/usr/bin/env python3

from puzzle4 import TOP, LEFT, RIGHT, BOTTOM, bruteforce, humanize

CONSTRAINTS = {
    0: [ (2, BOTTOM) ],

    1: [ (2, RIGHT ), (5, BOTTOM)                          ],
    2: [ (0, TOP   ), (1, LEFT  ), (3, RIGHT), (6, BOTTOM) ],
    3: [ (2, LEFT  ), (7, BOTTOM)                          ],

    4: [ (5, RIGHT )                        ],
    5: [ (1, TOP   ), (4, LEFT), (6, RIGHT) ],
    6: [ (2, TOP   ), (5, LEFT), (7, RIGHT) ],
    7: [ (3, TOP   ), (6, LEFT), (8, RIGHT) ],
    8: [ (7, LEFT  )                        ],
}

solutions = bruteforce(9, CONSTRAINTS)
print("First solution:", humanize(solutions[0]))
print("Number of solutions:", len(solutions))

# for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
#     print(id, ":", humanize(solution))

