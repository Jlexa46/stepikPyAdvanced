def gematria(word):
    return sum([ord(c.upper()) - ord('A') for c in word])


print(*sorted([input() for _ in range(int(input()))], key=lambda x: (gematria(x), x)), sep='\n')
