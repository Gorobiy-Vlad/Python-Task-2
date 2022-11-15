# 1.Написать функцию, принимающую один аргумент.
# Функция должна вывести на экран (c помощью print) тип данных этого аргумента (type)
def print_type(x):
    print(type(x))


a = 12
print_type(a)
b = 1.2
print_type(b)
c = "Hello"
print_type(c)
d = False
print_type(d)
print("*" * 100)


# 2.Написать функцию, принимающую два аргумента. Функция должна
# - если оба аргумента относятся к числовым типам (int, float) - вернуть их произведение
# - если к строкам - соединить в одну строку и вернуть
# - если первый строка, а второй нет - вернуть словарь (dict), в котором ключ - первый аргумент, значение - второй
# - в любом другом случае вернуть кортеж (tuple) из аргументов

def foo(x, y):
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        return x + y
    elif type(x) == str and type(y) == str:
        return x + y
    elif type(x) == str and type(y) != str:
        return {x: y}
    else:
        return (x, y)


value_a = 11
value_b = 125
print(foo(value_a, value_b))  # результат - сложение значений
value_a = "11"
value_b = "125"
print(foo(value_a, value_b))  # результат - обьединением двух строк
value_a = "A"
value_b = 123
print(foo(value_a, value_b))  # результат - формирование словаря из значений
value_a = 132
value_b = "FGDdfg"
print(foo(value_a, value_b))  # результат - формирования кортежа из значений

print("*" * 100)


# 3.Дан словарь продавцов и цен на какой то товар у разных продавцов: {
# ‘citrus’: 47.999,
# ‘istudio’ 42.999,
# ‘moyo’: 49.999,
# ‘royal-service’: 37.245,
# ‘buy.ua’: 38.324,
# ‘g-store’: 37.166,
# ‘ipartner’: 38.988,
# ‘sota’: 37.720
# }.
# Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный диапазон.
# Функция должна принимать словарь, начало и конец диапазона и возвращать список имен.

def search(beginning, end, my_dict):
    lst_names_seller = []
    for keys in my_dict.keys():
        if my_dict[keys] >= beginning and my_dict[keys] <= end:
            lst_names_seller.append(keys)
    return lst_names_seller


my_dict_a = {
    "citrus": 47.999,
    "istudio": 42.999,
    "moyo": 49.999,
    "royal-service": 37.245,
    "buy.ua": 38.324,
    "g-store": 37.166,
    "ipartner": 38.988,
    "sota": 37.720
}
print(search(37.700, 39.000, my_dict_a))

