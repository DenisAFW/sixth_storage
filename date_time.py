# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from datetime import datetime as dt
from sys import argv

__all__ = ['check_date', '_leap_year']


# value = input('Введите дату в формате DD.MM.YYYY -> ')


def check_date(date_value: str) -> bool:
    try:
        value = dt.strptime(date_value, "%d.%m.%Y").date()
        return True
    except:
        return False


def _leap_year(data_value: str) -> bool:
    year = int(data_value.split(".")[-1])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def res_date(date_value: str):
    if check_date(date_value):
        return 'Год високосный' if _leap_year(date_value) else 'Год не високосный'
    else:
        return 'Дата введена некорректно!'


# if __name__ == '__main__':
#     print(res_date('15.12.1985'))

if __name__ == "__main__":
    if len(argv) == 2:
        _, date = argv
        print(res_date(date))
    else:
        print("Дата для проверки не указана!")
