"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    # pass
    return '*' * 10


print('\nФункция simple_separator')  # Наименование вызываемой функции
print(simple_separator() == '**********')  # True


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    # pass
    return '*' * count


print('\nФункция long_separator')  # Наименование вызываемой функции
print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    # pass
    return simbol * count


print('\nФункция separator')  # Наименование вызываемой функции
print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    # pass
    print('**********' + '\n\n' +
          'Hello World!' + '\n\n' +
          '##########')


'''
**********

Hello World!

##########
'''
print('\nФункция hello_world')  # Наименование вызываемой функции
hello_world()


def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    # pass
    print('**********' + '\n\n' +
          f'Hello {who}!' + '\n\n' +
          '##########')


'''
**********

Hello World!

##########
'''
print('\nФункция hello_who')  # Наименование вызываемой функции
hello_who()
'''
**********

Hello Max!

##########
'''
print('\nФункция hello_who')  # Наименование вызываемой функции
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
print('\nФункция hello_who')  # Наименование вызываемой функции
hello_who('Kate')


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power
    (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    # pass
    result = 0
    for i in args:
        result += i
    return result ** power


print('\nФункция pow_many')  # Наименование вызываемой функции
print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


# Функция pow_many_2 - это дополнительно
# написано с использованием штатной функции sum.
# В исходном задании это отсутсвует.
def pow_many_2(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power
    (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    # pass
    return sum(args) ** power


print('\nФункция pow_many_2')  # Наименование вызываемой функции
print(pow_many_2(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many_2(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many_2(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many_2(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many_2(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


# Функция pow_many_3 - это дополнительно
# написано с использованием функции reduce() модуля functools.
# В исходном задании это отсутсвует.
# Подробнее о функции reduce():
# Источник: https://docs-python.ru/standart-library/modul-functools-python/funktsija-reduce-modulja-functools/
# Синтаксис:
#     reduce(function, iterable[, initializer])
# Параметры:
#     function - пользовательская функция, принимающая 2 аргумента,
#     iterable - итерируемая последовательность,
#     initializer - начальное значение.
# Возвращаемое значение:
#     требуемое единственное значение.
# Описание:
# Функция reduce() модуля functools кумулятивно применяет функцию function к
# элементам итерируемой iterable последовательности, сводя её к единственному значению.
#
# function это это функция которую требуется применить к элементам последовательности.
# Должна принимать два аргумента, где первый аргумент - аккумулированное ранее значение,
# а второй аргумент следующий элемент последовательности.
#
# iterable представляет собой последовательность, элементы которой требуется свести
# к единственному значению. Если последовательность пуста и не задан аргумент
# initializer, то возбуждается исключение TypeError.
#
# Например reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) вычисляет ((((1 + 2) +3) +4) +5).
# Левый аргумент x - это накопленное значение, а правый аргумент y - это
# следующий элемент iterable.
#
# Если присутствует необязательный initializer, он помещается перед
# элементами iterable в вычислении. Другими словами это базовое значение,
# с которого требуется начать отсчёт. Аргумент initializer, так же служит
# значением по умолчанию, когда iterable является пустым.
from functools import reduce


def pow_many_3(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power
    (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    # pass
    return reduce(lambda x, y: x + y, args) ** power


print('\nФункция pow_many_3')  # Наименование вызываемой функции
print(pow_many_3(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many_3(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many_3(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many_3(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many_3(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в виде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    # pass
    for k, v in kwargs.items():
        print(f'{k} --> {v}')


"""
name --> Max
age --> 21
"""
print('\nФункция print_key_val')  # Наименование вызываемой функции
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print('\nФункция print_key_val')  # Наименование вызываемой функции
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True,
    то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    # pass
    return list(filter(function, iterable))


print('\nФункция my_filter')  # Наименование вызываемой функции
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
