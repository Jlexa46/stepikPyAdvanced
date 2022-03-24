text = input()
print(int(text[::-1]) if len(text) <= 5 else int(text[:len(text) - 5] + text[len(text):len(text) - 6:-1]))
