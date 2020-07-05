
def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    even_int_list = list(i for i in range(100) if not i % 2)

    print(even_int_list)

    even_int_list = None
    return even_int_list


even_int_generator()

