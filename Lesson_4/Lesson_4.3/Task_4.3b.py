number = int(input())
list = [0] * number
for i in range(number):
    list[i] = [j for j in range(1, i + 2)]
print(*list, sep='\n')

# modified
# number = int(input())
# list = [[j for j in range(1, i + 2)] for i in range(number)]
# print(*list, sep='\n')
