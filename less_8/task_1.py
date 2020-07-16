"""
Напишите функцию, которая читает и распечатывает текстовый файл.
Напишите декоратор к этой функции, который печатает название файла и количество слов в нем
"""


def decorator(func):
    def wrapper(*args):
        direct_file = args[0]
        name_file = direct_file.split('\\')[-1]
        print(f'Название файла: {name_file}')
        with open(direct_file, encoding='utf8') as file:
            cnt_word = len(file.read().split())
            print(f'Количество слов в файле: {cnt_word}')
        return func(*args)

    return wrapper


@decorator
def list_file_direct(direct_file):
    with open(direct_file, encoding='utf8') as file:
        print(file.read())


list_file_direct('.\\test_file.txt')