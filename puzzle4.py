#!/usr/bin/env python3

PATETA_UP = +1
PLUTO_UP  = +2
MICKEY_UP = +3
MINNIE_UP = +4

PATETA_DOWN = -1
PLUTO_DOWN  = -2
MICKEY_DOWN = -3
MINNIE_DOWN = -4

TOP    = 2
BOTTOM = 0
LEFT   = 3
RIGHT  = 1

MIRROR = {
    TOP   : BOTTOM,
    BOTTOM: TOP   ,
    LEFT  : RIGHT ,
    RIGHT : LEFT  ,
}

KEYS = [
    (MINNIE_DOWN, PATETA_UP, MINNIE_DOWN, PLUTO_UP),
    (PATETA_UP, MINNIE_DOWN, PLUTO_UP, MICKEY_DOWN), # REPEATED
    (MINNIE_DOWN, PATETA_UP, PLUTO_DOWN, MICKEY_UP),
    (MICKEY_UP, PLUTO_DOWN, MICKEY_UP, PATETA_DOWN),
    (MICKEY_UP, PLUTO_DOWN, MINNIE_UP, PATETA_DOWN),
    (MINNIE_UP, PLUTO_DOWN, MICKEY_UP, PATETA_DOWN),
    (PATETA_UP, PLUTO_DOWN, MINNIE_UP, MICKEY_DOWN),
    (PATETA_UP, MINNIE_DOWN, PLUTO_UP, MICKEY_DOWN), # REPEATED
    (PATETA_DOWN, MINNIE_UP, MICKEY_DOWN, PLUTO_UP),
]

KEY_NAMES = {
    1: "P",
    2: "C",
    3: "M",
    4: "I",

    -1: "p",
    -2: "c",
    -3: "m",
    -4: "i",
}

def humanize(key):
    if isinstance(key, list):
        return " ".join([humanize(x) for x in key])
    else:
        return KEY_NAMES[key[0]] + KEY_NAMES[key[1]] + KEY_NAMES[key[2]] + KEY_NAMES[key[3]]
    
def shift_rotate(keys, value):
    return keys if value == 0 else keys[value:] + keys[:value]

def check_constraints(state, i, constraints):
    for other, position in constraints[i]:
        if other >= i:
            continue
        if other >= len(state):
            continue
        if state[other] is None:
            continue
        if state[i][position] == -state[other][MIRROR[position]]:
            continue
        return False
    return True

def _bruteforce(state, keys, used, i, constraints, solutions):
    if i == len(state):
        solutions.append([x for x in state])
        return

    for k, key in enumerate(keys):
        if used[k]:
            continue

        used[k] = True

        for rotate in range(4):
            key = shift_rotate(key, rotate)
            state[i] = key

            if check_constraints(state, i, constraints):
                _bruteforce(state, keys, used, i+1, constraints, solutions)

        used[k] = False
    state[i] = None

def bruteforce(max_state, constraints):
    state = [None for _ in range(max_state)]
    used  = [False for _ in KEYS]
    solutions = []
    _bruteforce(state, KEYS, used, 0, constraints, solutions)
    return solutions
