tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []
for i in range(len(tuples)):
    if len(tuples[i]) > 0:
        non_empty_tuples.append(tuples[i])
print(non_empty_tuples)

# modified
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [i for i in tuples if i]
# print(non_empty_tuples)
