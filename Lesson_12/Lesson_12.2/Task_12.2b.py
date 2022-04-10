def generate_index():
    from string import ascii_uppercase, digits
    from random import choice
    return choice(ascii_uppercase) + choice(ascii_uppercase) + choice(digits) + choice(digits) + '_' + choice(digits) + choice(digits) + choice(ascii_uppercase) + choice(ascii_uppercase)
