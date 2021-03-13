def main(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        if len(argv) == 2:
            f.write(f'{argv[1]}{chr(10)}')
        else:
            return 'Недостаточно аргументов'

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))