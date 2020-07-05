
enter_str_1 = '1111'
enter_str_2 = '222'


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """

    result_str = str1[:int(len(str1)/2)] + str2 + str1[int(len(str1)/2):]

    print(result_str)

    result_str = None
    return result_str


mix_strings(enter_str_1,enter_str_2)