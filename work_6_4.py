# Задание 4
def make_file_from_files(source_file1, source_file2, dest_file):
    with open(source_file1, encoding='utf-8') as users:
        with open(source_file2, encoding='utf-8') as hobby:
            with open(dest_file, 'w', encoding='utf-8') as dest:
                for user in users:
                    hobby_line = hobby.readline().replace('\n','')
                    dest.write(f'{user.replace(chr(10),"")}: {hobby_line if hobby_line else None}{chr(10)}')
            return (1 if hobby.readline() else 0)

print(f'Код завершения скрипта: {make_file_from_files("users.csv", "hobby.csv", "users_hobby.txt")}')
