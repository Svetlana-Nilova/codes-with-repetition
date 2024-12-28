"""
Задание.

Fizz-Buzz - это известная игра, помогающая детям освоить в игровой форме правила деления. Участники садятся в круг, чтобы игра теоретически могла продолжаться бесконечно. Первый игрок говорит «Один» и передает ход тому, кто слева. Каждый следующий игрок должен мысленно прибавить к предыдущему числу единицу и произнести либо его, либо одно из ключевых слов: Fizz, если число без остатка делится на три, или Buzz, если на пять. Если соблюдаются оба этих условия, он произносит Fizz-Buzz. 8 Игрок, не сумевший сказать правильное слово, выбывает из игры. Последний оставшийся игрок признается победителем.
Разработайте программу, реализующую алгоритм игры Fizz-Buzz применительно к первым 100 числам. Каждый следующий ответ должен отображаться на новой строке.
"""



"""
Атрибуты модуля
    Методы:
        fizz_buzz(number) - Реализует алгоритм игры Fizz-Buzz к первым 100 числам.
        main() - Обеспечивает интерфейс при реализации алгоритма игры Fizz-Buzz.

    Константы:
        HELLO: str - текстовая строка с назначением программы.
"""


HELLO = "Программа выводит алгоритм игры Fizz-Buzz применительно к первым 100 числам."


def fizz_buzz(number: int) -> list:
    """
    Реализует алгоритм игры Fizz-Buzz к первым 100 числам.

    Параметры метода:
        number: int - число до которого идет игра.

    Возврат:
        result_list: list - список результатов игры Fizz-Buzz.
    """

    result_list = []
    
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            result_list.append('Fizz-Buzz')
        elif i % 3 == 0:
            result_list.append('Fizz')
        elif i % 5 == 0:
            result_list.append('Buzz')
        else:
            result_list.append(str(i))

    return result_list


def main():
    """
    Обеспечивает интерфейс при реализации алгоритма игры Fizz-Buzz.

    Переменные метода:
        hund: int - число до которого идет игра.
        result_list: list – список результатов игры Fizz-Buzz.
    """

    print(HELLO)

    hund = 100
    result_list = fizz_buzz(hund)

    for i in result_list:
        print(i)


main()
