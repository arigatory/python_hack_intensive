import requests

urls = ['https://skillbox.ru/',
        'https://habr.com/ru/',
        'https://www.python.org/',
        'https://stackoverflow.com/',
        'https://realpython.com/',
        'https://www.tinkoff.ru/',
        'https://www.vtb.com/o-banke/']
for url in urls:
    response = requests.get(url)
    for i in range(100):
        if response.status_code == 200:
            print(url, response.status_code)
            break