def coincidence(t = None, r: range = None):
    if t is None or r is None: return []
    list = []
    for i in t: 
        if isinstance(i, (int, float)) and r.start <= i < r.stop:
            list.append(i)
    return list

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))            # => [3, 4, 5]
print(coincidence())                                         # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]