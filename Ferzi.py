# # Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# # Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# # на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
# # число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#
# # Такое точно было на семинаре?
from random import randrange

# Создаем множество для исключения похожих координат
coordinates = {(randrange(1, 9), randrange(1, 9)) for i in range(0, 8)}


# Проверяем размер множества и пересоздаем в случае несоответствия
def check_identical(coordinates):
    while len(coordinates) != 8:
        coordinates = {(randrange(1, 9), randrange(1, 9)) for i in range(0, 8)}
    return coordinates


def check_defeat(coordinates):
    count = 0
    if check_identical(coordinates):
        new_coordinates = list(coordinates)
        for i in range(len(new_coordinates)):
            for j in range(i + 1, len(new_coordinates)):
                count += 1
                print(f'{count = } - Количество несовпадений ')
                if new_coordinates[i][0] == new_coordinates[j][0] or new_coordinates[i][1] == new_coordinates[j][1]:
                    return True
    else:
        'Увы'
    return False


print(check_defeat(coordinates))
