def check_password(__pswd):
    import string
    correct = all([(set(__pswd) & set(string.ascii_lowercase)) != set(),
                   (set(__pswd) & set(string.ascii_uppercase)) != set(),
                   (set(__pswd) & set(string.digits)) != set(),
                   len(__pswd) >= 7])
    return 'YES' if correct else 'NO'


print(check_password(input()))

