def reverse_vowels(s: str) -> str:
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    l = 0
    r = len(s)-1
    
    while (r > l):
        if (s[l] in vowels and s[r] in vowels):
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1
        elif (s[l] in vowels and s[r] not in vowels):
            r -= 1
        elif (s[l] not in vowels and s[r] in vowels):
            l += 1
        else:
            r -= 1
            l += 1

    return ''.join(s)

print(reverse_vowels('mewing'))
