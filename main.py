import random


def generate_good_password(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'\
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
               '0123456789!@#$%^&*()_+<>?,.'
    # password = ''
    # for i in range(length):
    #     password += random.choice(alphabet)
    # return password
    return ''.join(random.choices(alphabet, k=length))

print(generate_good_password(10))
print(generate_good_password(20))
print(generate_good_password(10))