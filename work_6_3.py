# Задание 3
import pickle

def make_dict_from_files(source_file1, source_file2, dest_file):
    database = {}
    with open(source_file1, encoding='utf-8') as users:
        with open(source_file2, encoding='utf-8') as hobby:
            for user in users:
                hobby_line = hobby.readline().replace('\n','')
                database[user.replace(',', ' ').replace('\n','')] = hobby_line if hobby_line else None
            with open(dest_file, 'wb') as dest:
                pickle.dump(database, dest)
            return (1 if hobby.readline() else 0)

print(f'Код завершения скрипта: {make_dict_from_files("users.csv", "hobby.csv", "file_6-3.bin")}')

# Проверка бинарного файла
print('Загруженные данные:')
with open("file_6-3.bin", 'rb') as f:
    print(pickle.load(f))

