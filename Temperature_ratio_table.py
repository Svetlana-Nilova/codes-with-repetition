"""
Задание

Напишите программу для вывода таблицы соотношения температур, выраженных в градусах Цельсия и Фаренгейта. В таблице должны размещаться все температуры между 0 и 100 градусами Цельсия, кратные 10. Дополните таблицу подходящими заголовками. Формулу для перевода температуры из градусов Цельсия в градусы Фаренгейта можно легко найти на просторах интернета.
"""



"""
Атрибуты модуля
    Методы:
        list_temperature(temp_start, temp_end, step) - формирует список соотношения температур градусов Цельсия и Фаренгейт.
        convert_celsia_to_farengeit(temp_celsia) - преобразует температуру из градусов Цельсия в градусы Фаренгейта.
        main() - Обеспечивает интерфейс при формировании таблицы температур в градусах Цельсия и Фаренгейта.

    Константы:
        HELLO: str - текстовая строка с назначением программы.
"""


HELLO = "Программа выводит таблицу температур в градусах Цельсия и Фаренгейта"


def list_temperature(temp_start: float, temp_end: float, step: float) -> list:
    """
    Формирует список соотношения температур градусов Цельсия и Фаренгейта.

    Параметры метода:
        temp_start: float - начальная температура.
        temp_end: float - конечная температура.
        step: float - шаг температур.

    Переменные метода:
        temp_current_list: list[float] - хранит текущие (промежуточные) температуры Цельсия и соответствующую температуру Фаренгейта.
        temp_current: float - текущие (промежуточное) значение в градусах Цельсия.

    Возврат:
        temp_list: list[list[float]] -  список температур, градусы Цельсия в 0 индексе каждого элемента, градусы Фаренгейта в 1 индексе каждого элемента.

    """

    temp_list = []
    temp_current_list = ["C", "F"]
    temp_current = temp_start

    while temp_current <= temp_end:
        temp_current_list[0] = temp_current
        temp_current_list[1] = convert_celsia_to_farengeit(temp_current_list[0])

        temp_list.append(temp_current_list.copy())
        temp_current += step

    return temp_list

def convert_celsia_to_farengeit(temp_celsia: float) -> float:
    """
    Переводит температуру из градусов Цельсия в градусы Фаренгейта.

    Параметры метода:
        temp_celsia: float - градусы Цельсия для перевода в Фаренгейт.

    Возврат:
        temp_farengeit: float - градусы Фаренгейта соответствующие полученным градусам Цельсия.
    """

    temp_farengeit = 1.8 * temp_celsia + 32

    return temp_farengeit


def main():
    """
    Обеспечивает интерфейс при формировании таблицы температур в градусах Цельсия и Фаренгейта.

    Переменные метода:
        temp_start: float - начальная температура.
        temp_end: float - конечная температура.
        step: float - шаг температур.
        temp_list: list[list[float]] - список температур, градусы Цельсия в 0 индексе каждого элемента, градусы Фаренгейта в 1 индексе каждого элемента.
    """

    print(HELLO)

    temp_start = 0
    temp_end = 100
    step = 10

    temp_list = ["EP"]*len(list_temperature(temp_start, temp_end, step))
    temp_list = list_temperature(temp_start, temp_end, step)

    print("градусы Цельсия     градусы Фаренгейта")
    for i in temp_list:
        print("{:7.1f}     {:15.1f}".format(i[0], i[1]))


main()
