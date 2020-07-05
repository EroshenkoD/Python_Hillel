
enter_list = ['/catalog/', '0/catalog/e', '1111/catalog/', '0111', '1111']


def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    result_list = []

    for i in url_list:

        if i.find('/catalog/') + 1:
            result_list.append(i)

    print(result_list)

    result_list = None
    return result_list


catalog_finder(enter_list)
