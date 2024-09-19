import re

def count_words(line: str):
    line = [x.lower() for x in re.findall(r'\b\w+\b', line)]
    dict1 = dict.fromkeys(line, 0)
    for a in line: dict1[a] += 1
    return dict1

count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo")              # => {"doo": 3, "bee": 2}