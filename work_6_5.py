# Задание 5
def main(argv):
    from work_6_4 import make_file_from_files
    return 'Недостаточно аргументов' if len(argv) < 4 else make_file_from_files(*argv[1:])

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))

