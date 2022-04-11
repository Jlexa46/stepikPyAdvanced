from decimal import Decimal
d = Decimal(input())
d = d.exp() + d.ln() + d.log10() + d.sqrt()
print(d)
