_text = input().split()
print(*[_text[0:i].count(_text[i]) + 1 for i in range(len(_text))])
