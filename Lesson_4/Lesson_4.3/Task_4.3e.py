lst = []
text = input().split()
lst.append(list(text[0]))
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        lst[-1] += text[i]
    else:
        lst.append(list(text[i]))
print(lst)
