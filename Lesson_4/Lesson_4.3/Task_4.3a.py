number = int(input())
list = [0] * number
for i in range(number):
    list[i] = [_ for _ in range(1, number + 1)]
print(*list, sep='\n')

# modified
# number = int(input())
# list = [[i for i in range(1, number + 1)] for _ in range(number)]
# print(*list, sep='\n')
