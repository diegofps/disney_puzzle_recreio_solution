#!/usr/bin/env python3

from puzzle3 import BASE, RIGHT, LEFT, bruteforce, humanize

CONSTRAINTS = {
    0: [ (2, BASE  )                        ],
    1: [ (2, RIGHT )                        ],
    2: [ (0, BASE  ), (1, RIGHT), (3, LEFT) ],
    3: [ (2, LEFT  )                        ],

    4: [ (6, BASE  )                        ],
    5: [ (6, RIGHT )                        ],
    6: [ (4, BASE  ), (5, RIGHT), (7, LEFT) ],
    7: [ (6, LEFT  )                        ],
}

solutions = bruteforce(9, CONSTRAINTS)
print("First solution:", humanize(solutions[0]))
print("Number of solutions:", len(solutions))

# for id, solution in enumerate(bruteforce(8, CONSTRAINTS)):
#     print(id, ":", humanize(solution))