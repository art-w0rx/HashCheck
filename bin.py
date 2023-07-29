# программа HachCheck предназначена для проверки хэш суммы 
# двух файлов.

import hashlib
import os

os.chdir('files')

def calculate_hash(filename):
    # Создаем объект хэша (в данном случае используется алгоритм SHA256)
    hash_object = hashlib.sha256()

    # Открываем файл в бинарном режиме и вычисляем хэш
    with open(filename, 'rb') as file:
        # Читаем файл по частям для эффективного вычисления хэша
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)

    # Возвращаем полученную хэш-сумму в виде строки
    return hash_object.hexdigest()

def compare_hashes(file1, file2):
    # Вычисляем хэш-суммы для обоих файлов
    hash1 = calculate_hash(file1)
    hash2 = calculate_hash(file2)
    print("Хэш первого файла:", hash1)
    print("Хэш второго файла:", hash2)

    # Сравниваем хэш-суммы и выводим результат
    if hash1 == hash2:
        print("\n\033[32mХэш совпадает(Верно)\033[0m")
    else:
        print("\n\033[31mХэш НЕ СОВПАДАЕТ(НЕВЕРНО)\033[0m")

#Блок работы с интерфейсом начального меню
def menu():
    print_files = os.listdir()
    print("\nФайлы:", print_files)
    menu_inp = input("\n'Enter'-Начать / '1'-Выйти\nВвод: ")
    if menu_inp =='1':
        os.system('clear')
        exit()
    else:
        start()

# Пример использования        
def start():
    try:
        req_file1 = input("\nВведите имя первого файла: ")
        req_file2 = input ("Введите имя второго файла: ")
        compare_hashes(req_file1, req_file2)
    except FileNotFoundError:
        print("\n\033[33mФайл не найден! Повторите попытку!\033[0m")
        menu()
    next_do = input("\n'Enter'-Продолжить / '1'-Выйти \nВвод: ")
    if next_do == '1':
        os.system('clear')
        exit()
    else:
        menu()
    
menu()
