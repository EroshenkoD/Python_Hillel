def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    biggest_ints = list()
    data_set = set(input_list)

    for _ in range(3):
        biggest_ints.append(max(data_set))
        data_set.remove(max(data_set))

    return biggest_ints


enter_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
three_biggest_int(enter_list)


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    lowest_int_index = input_list.index(min(input_list))
    return lowest_int_index


enter_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
lowest_int_index(enter_list)


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    input_list.reverse()
    reversed = input_list
    return reversed


enter_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
reversed_list(enter_list)


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    common_keys = list()
    for i in dict1.keys():
        if dict2.get(i, 0):
            common_keys.append(i)

    return common_keys


enter_dict1 = {'1': 1, '2': 2}
enter_dict2 = {'2': 2, '3': 3}
find_common_keys(enter_dict1, enter_dict2)


def sort_by_age(student_list):
    """
    Дан массив из словарей. C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """
    student_list.sort(key=lambda i: i['age'])

    sorted_dict = {}

    for j in student_list:

        if not j['city'] in sorted_dict:
            sorted_dict[j['city']] = []
        sorted_dict[j['city']].append({'name': j['name'], 'age': j['age']})

    return sorted_dict


enter_list = [{'name': 'Andrey', 'age': 34, 'city': 'Kiev'}, {'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
              {'name': 'Artem', 'age': 50, 'city': 'Dnepr'}, {'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
              {'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}, {'name': 'Vladimir', 'age': 32, 'city': 'Lviv'}]
sort_by_age(enter_list)
