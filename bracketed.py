#count pair bracket and return true
PAIRINGS = {
    '(': ')'
}


def bracketed(symbols):
    stack = []
    for s in symbols:
        if s in PAIRINGS:
            stack.append(s)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:  # too many closing symbols
            return False
        if s != PAIRINGS[expected_opening_symbol]:  # mismatch
            return False
    return len(stack) == 0  # false if too many opening symbols

print(is_balanced('(a+b)'))