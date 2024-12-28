"""
Задание.

В зоопарке цена входного билета зависит от возраста посетителя. Дети до двух лет допускаются бесплатно. Дети в возрасте от трех до 12 лет могут посещать зоопарк за $14,00. Пенсионерам старше 65 лет вход обойдется в $18,00, а обычный взрослый билет стоит $23,00.
Напишите программу, которая будет запрашивать возраст всех посетителей в группе (по одному за раз) и выводить общую цену билетов для посещения зоопарка этой группой. В качестве индикатора окончания ввода можно по традиции использовать пустую строку. Общую цену билетов стоит выводить в формате с двумя знаками после запятой.
"""



"""
Атрибуты модуля
    Методы:
        def calculate_ticket_price(age) - Определяет стоимость билета по возрасту покупателя.
        main() - Обеспечивает интерфейс при вычислении суммы цен билетов.

    Константы:
        HELLO: str - текстовая строка с назначением программы.
"""


HELLO = "Программа определяет общую стоимость билетов по возрасту посетителя."


def calculate_ticket_price(age: int) -> float:
    """
    Определяет стоимость билета по возрасту покупателя.
    
    Параметры метода:
        age: int - возраст посетителя.
    
    Возврат:
        price: float - цена билета.
    """
    
    if age <= 2:
        price = 0.0
    elif 3 <= age <= 12:
        price = 14.00
    elif age > 65:
        price = 18.00
    else:
        price = 23.00
        
    return price


def main():
    """
    Обеспечивает интерфейс при вычислении суммы цен билетов.
    
    Переменные метода:
        flag: bool - переменная для работы и остановки бесконечного цикла .
        age_input: str - ввод возраста посетителя.
        total_price: int - общая стоимость билетов.
    """

    print(HELLO)

    total_price = 0.0
    flag = True
    
    while flag == True:

        age_input = input("Введите возраст посетителя(пустая строка для окончания ввода): ")
        
        if age_input == "":
            flag = False
        else:
            age = int(age_input)
            ticket_price = calculate_ticket_price(age)
            total_price += ticket_price
    
    print(f"Общая цена билетов: ${total_price:.2f}")


main()
