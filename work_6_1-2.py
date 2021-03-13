# Загрузка данный с сайта в файл
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    from requests import get, utils
    response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    f.write(content)

print('# Задание 1')

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        _ = line.replace('"','').split(' ')
        print((_[0], _[5], _[6]))

print('# Задание 2')

with open('nginx_logs.txt', encoding='utf-8') as f:
    spam_base = {}
    for line in f:
        ip = line[:line.find(' ')]
        spam_base[ip] = spam_base.get(ip) + 1 if spam_base.get(ip) else 1
    l = list(spam_base.items())
    l.sort(key=lambda i: i[1])
    print(f'Спам с адреса {l[-1][0]} в количестве {l[-1][1]} обращений')
