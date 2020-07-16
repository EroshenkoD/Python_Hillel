"""
1. Напишите функцию, которая возвращает список файлов из директории.
2. Напишите декоратор для этой функции, который распечатает все файлы с
раcширением .log из найденных
"""
import os


def decorator(func):
    def wrapper(*args):
        direct = args[0]
        rez = func(*args)
        for i in rez:
            if '.log' in i:
                with open(f'{direct}\{i}') as file:
                    print(file.read())

        return rez
    return wrapper


@decorator
def list_file_direct(direct):
    return os.listdir(path=direct)


list_file_direct('C:\ProgramData')
