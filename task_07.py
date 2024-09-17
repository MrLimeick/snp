def combine_anagrams(words):
    anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word.lower()))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
            
    return list(anagrams.values())

# Пример использования
result = combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
print(result)  # Вывод: [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['creams', 'scream'], ['four']]
