
enter_str = '123456789'


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """

    if len(input_str) % 2:
        output_str = str(input_str[int(len(input_str)/2)-1:int(len(input_str)/2)+2])
    else:
        output_str = str(input_str[int(len(input_str)/2) - 1:int(len(input_str)/2) + 1])
    print(output_str)
    output_str = None
    return output_str


get_str_center(enter_str)