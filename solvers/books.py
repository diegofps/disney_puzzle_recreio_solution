#!/usr/bin/env python3

from puzzle4 import TOP, LEFT, RIGHT, BOTTOM, bruteforce, humanize

CONSTRAINTS = {
    0: [ (1, RIGHT )                                       ],
    1: [ (0, LEFT  ), (2, RIGHT ), (3, BOTTOM)             ],
    2: [ (1, LEFT  ), (4, BOTTOM)                          ],
    
    3: [ (1, TOP   ), (4, RIGHT ), (7, BOTTOM)             ],
    4: [ (2, TOP   ), (3, LEFT  ), (5, RIGHT), (8, BOTTOM) ],
    5: [ (4, LEFT  )                                       ],

    6: [ (7, RIGHT )                                       ],
    7: [ (3, TOP   ), (6, LEFT ), (8, RIGHT)               ],
    8: [ (4, TOP   ), (7, LEFT )                           ]
}

for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
    print(id, ":", humanize(solution))

