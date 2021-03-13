'''
def main(argv):
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        if len(argv) == 3:
            for i, line in enumerate(f, 1):
                if i == int(argv[1]):
                    print (i, line)
                    f.write(f'{argv[2]}{chr(10)}')
                    break
        else:
            return 'Недостаточно аргументов'
'''

'''
import fileinput

def main(argv):
    if len(argv) == 3:
        with fileinput.input('bakery.csv', inplace=True) as f:
            for i, line in enumerate(f, 1):
                if i == int(argv[1]):
                    _ = line.replace(line, argv[2])
                    print(_, end='')
                    break
    else:
        return 'Недостаточно аргументов'

'''
def main(argv):
    return None

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))