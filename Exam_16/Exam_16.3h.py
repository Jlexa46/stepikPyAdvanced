def arithmetic_operation(operation):
    import operator
    return {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}[operation]
