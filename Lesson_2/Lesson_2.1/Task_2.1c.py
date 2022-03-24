def pay_by_symbol(text, payments):
    cache = len(text) * payments
    return '0 р. ' + str(cache) + ' коп.' if cache <= 99 else str(cache // 100) + ' р. ' + str(cache % 100) + ' коп.'


print(pay_by_symbol(input(), 60))
