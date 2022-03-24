text, sac_number = input(), ''
if len(text) <= 3:
    print(text)
else:
    for i in range(-1, -len(text) - 1, -1):
        sac_number += text[i] if i % 3 != 0 else text[i] + ','
    sac_number = sac_number[::-1] if sac_number[-1] != ',' else sac_number[-2::-1]
print(sac_number)
