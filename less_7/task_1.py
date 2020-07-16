
enter_str = 'qqqwweerrrt'


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = dict()

    for i in input_str:
        if i in output_dict.keys():
            output_dict[i] += 1
        else:
            output_dict[i] = 1

    print(output_dict)
    output_dict = None
    return output_dict


count_symbols(enter_str)
