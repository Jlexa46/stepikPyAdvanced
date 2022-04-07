words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {w: [ord(c) for c in w] for w in words}
