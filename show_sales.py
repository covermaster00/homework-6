def main(argv):
    with open('bakery.csv', encoding='utf-8') as f:
        if len(argv) == 1:
            print(f.read())
        elif len(argv) == 2:
            for i, line in enumerate(f, 1):
                if i >= int(argv[1]):
                    print(line, end='')
                    break
            print(f.read())
        elif len(argv) == 3:
            for i, line in enumerate(f, 1):
                if i >= int(argv[1]) and i <= int(argv[2]):
                    print(line, end='')
                elif i > int(argv[2]):
                    break
        else:
            return 'Недостаточно аргументов'
        return None

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))