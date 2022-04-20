import string

is_non_negative_num = lambda x: not bool(set(x).difference(set(string.digits+'-.'))) and x.count('.') <= 1 and float(x) >= 0
