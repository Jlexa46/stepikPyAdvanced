def convert_ip(ip):
    return sum([int(num) * 256**i for i, num in enumerate(ip.split('.')[::-1])])

print(*sorted([input() for _ in range(int(input()))], key=lambda x: convert_ip(x)), sep='\n')
