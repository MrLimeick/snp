def max_odd(t):
    max = None
    for i in t:
        if isinstance(i, (float, int)) and i % 2 != 0 and i > max:
            max = i

    print(max)

max_odd([1, 2, 3, 4, 4])                  # => 3
max_odd([21.0, 2, 3, 4, 4])               # => 21
max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
max_odd(['ololo', 'fufufu'])              # => None
max_odd([2, 2, 4])                        # => None
