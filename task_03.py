def max_odd(t):
    if t is None: return None

    max = float('-inf')
    for i in t:
        if isinstance(i, (float, int)) and i % 2 != 0 and i > max:
            max = i

    if (max <= float('-inf')): return None
    else: return max