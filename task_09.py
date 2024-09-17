def getSum(dict):
    num = 0
    for i in dict.values(): num += i
    return num

def RemoveKeysLessThanTen(oldDict: dict):
    newDict = dict()
    for n in oldDict: 
        if oldDict[n] >= 10: newDict[n] = oldDict[n]
    return newDict

def connect_dicts(dict1: dict, dict2: dict):
    i1, i2 = getSum(dict1), getSum(dict2)
    dict1, dict2 = RemoveKeysLessThanTen(dict1), RemoveKeysLessThanTen(dict2)
    p = (dict1, dict2) if i1 <= i2 else (dict2, dict1)

    for (k, v) in p[1].items():
        p[0][k] = v
    
    d = dict(sorted(p[0].items(), reverse=True))
    print(d)

connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # => { "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # => {d:11,"c":12, "a":13}
connect_dicts({  "a": 14, "b": 12 }, { "c": 11,  "a": 15 })       # => { "c": 11, "b": 12,  "a": 15 }