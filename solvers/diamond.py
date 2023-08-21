#!/usr/bin/env python3

from puzzle3 import BASE, RIGHT, LEFT, bruteforce, humanize

CONSTRAINTS = {
    0: [ (1, RIGHT ), (5, BASE  ) ],
    1: [ (0, RIGHT ), (2, LEFT  ), (6, BASE) ],
    2: [ (1, LEFT  ), (3, BASE  ) ],
    3: [ (2, BASE  ), (4, RIGHT ) ],
    4: [ (3, RIGHT ), (5, LEFT  ), (7, BASE) ],
    5: [ (0, BASE  ), (4, LEFT  ) ],

    6: [ (1, BASE  ) ],
    7: [ (4, BASE  ) ],
}

for id, solution in enumerate(bruteforce(9, CONSTRAINTS)):
    print(id, ":", humanize(solution))
