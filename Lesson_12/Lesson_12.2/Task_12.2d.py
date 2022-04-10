from random import randint
tickets = set()
while len(tickets) != 100:
    ticket = randint(1000000, 9999999)
    tickets.add(str(ticket))
print(*tickets, sep='\n')
