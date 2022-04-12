from fractions import Fraction
f1, f2 = [input() for _ in range(2)]
print(f'{f1} + {f2} = {Fraction(f1)+Fraction(f2)}\n{f1} - {f2} = {Fraction(f1)-Fraction(f2)}\n{f1} * {f2} = {Fraction(f1)*Fraction(f2)}\n{f1} / {f2} = {Fraction(f1)/Fraction(f2)}')
