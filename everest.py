#!/usr/bin/env python3

from puzzle3 import BASE, RIGHT, LEFT, bruteforce, humanize

CONSTRAINTS = {
    0: [ (2, BASE )                        ],
    1: [ (5, BASE ), (2, RIGHT)            ],
    2: [ (0, BASE ), (1, RIGHT), (3, LEFT) ],
    3: [ (7, BASE ), (2, LEFT)             ],
    4: [ (5, RIGHT)                        ],
    5: [ (1, BASE ), (4, RIGHT), (6, LEFT) ],
    6: [ (7, RIGHT), (5, LEFT)             ],
    7: [ (3, BASE ), (6, RIGHT), (8, LEFT) ],
    8: [ (7, LEFT )                        ]
}

for solution in bruteforce(9, CONSTRAINTS):
    print(humanize(solution))
