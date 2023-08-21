#!/usr/bin/env python3

from puzzle3 import BASE, RIGHT, LEFT, bruteforce, humanize

CONSTRAINTS = {
    0: [ (1, LEFT )             ],
    1: [ (0, LEFT ), (2, BASE)  ],
    2: [ (1, BASE ), (3, LEFT ) ],
    3: [ (2, LEFT ), (4, BASE ) ],
    4: [ (3, BASE ), (5, LEFT)  ],
    5: [ (4, LEFT ), (6, BASE ) ],
    6: [ (5, BASE ), (7, LEFT)  ],
    7: [ (6, LEFT ), (8, BASE)  ],
    8: [ (7, BASE )             ],
}

for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
    print(id, ":", humanize(solution))
