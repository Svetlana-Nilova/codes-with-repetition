"""
Задание.

Создайте программу для расчета средней оценки по введённым значениям (оценка выставляется по американской 11 бальной системе оценивания) Для окончания ввода можно использовать индикатор в виде пустой строки. Точность вывода один знак после запятой. Например, если пользователь последовательно введет оценки A, затем C+, а после этого B и пустую строку, средний результат должен составить 3,1.
Никаких проверок на ошибки проводить не нужно. Предположим, что пользователь может вводить только корректные оценки или ноль. Информацию о системе оценивания можно найти на просторе интернет.
"""



"""
Атрибуты модуля
    Методы:
        main() - Обеспечивает интерфейс при вычислении средней оценки.
        calculate_average_grade() - Расcчитывает среднюю оценку по введённым значениям.
    
    Константы:
        HELLO: str - текстовая строка с назначением программы.
        GRADE_INPUT: str - Содержит текстовую строку поясняющую пользователю этап выполнения программы.
        DICT_OF_GRADE: dict - словарь оценок.  
"""


HELLO = "Программа выводит среднюю оценку по введеным значениям по американской системе оценивания"

GRADE_INPUT = "Введите оценку или пустую строку для завершения ввода: "

DICT_OF_GRADE = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0,
}


def calculate_average_grade(count: int, summ_score: float) -> float:
    """
    Рассчитывает среднюю оценку по введённым значениям.

    Параметры метода:
        count: int - счетчик кол-ва оценок.
        summ_score: float - сумма всех веденных оценок.

    Возврат:
        average: str - средняя оценка.
    """
    
    if count > 0:
        average = summ_score / count
        return average


def main():
    """
    Обеспечивает интерфейс при вычислении средней оценки по введеным значениям.
    
    Переменные метода:
        summ_score: float - сумма всех веденных оценок.
        count: int - счетчик кол-ва оценок.
        flag_input_grade: bool - переменная для работы и остановки цикла при вводе оценки.
        grade: str - введенная оценка.
        average_score: float - средняя оценка.
    """

    print(HELLO)

    summ_score = 0.0
    count = 0
    flag_input_grade = True
    
    while flag_input_grade == True:
        
        grade = input(GRADE_INPUT)
        
        if grade == "":  
            flag_input_grade = False
            
        if grade in DICT_OF_GRADE:  
            summ_score += DICT_OF_GRADE[grade]
            count += 1
    
    average_score = calculate_average_grade(count, summ_score)
    
    print(f"Средняя оценка: {average_score:.1f}")


main()
