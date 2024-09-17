replace_chars = [' ', '-', ',', '`', "'", "!"]

def is_palindrome(s):
    if type(s) != str: s = str(s)
    s = s.lower()
    for i in replace_chars: s = s.replace(i, '')
    l = len(s);
    for i in range(0, int(l / 2)):
        if s[i] != s[l - i - 1]:
            return False
    return True

print(is_palindrome("A man, a plan, a canal -- Panama"))  # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False