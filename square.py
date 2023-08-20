#!/usr/bin/env python3

from puzzle4 import TOP, LEFT, RIGHT, BOTTOM, bruteforce, humanize

CONSTRAINTS = {
    0: [ (1, RIGHT ), (3, BOTTOM)                          ],
    1: [ (0, LEFT  ), (2, RIGHT ), (4, BOTTOM)             ],
    2: [ (1, LEFT  ), (5, BOTTOM)                          ],
    3: [ (0, TOP   ), (4, RIGHT ), (6, BOTTOM)             ],
    4: [ (1, TOP   ), (3, LEFT  ), (5, RIGHT), (7, BOTTOM) ],
    5: [ (2, TOP   ), (4, LEFT  ), (8, BOTTOM)             ],
    6: [ (3, TOP   ), (7, RIGHT )                          ],
    7: [ (4, TOP   ), (6, LEFT  ), (8, RIGHT)              ],
    8: [ (5, TOP   ), (7, LEFT  )                          ]
}

for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
    print(id, ":", humanize(solution))

