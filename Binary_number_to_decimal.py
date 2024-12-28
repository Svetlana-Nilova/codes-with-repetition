"""
Задание.

Напишите программу, которая будет преобразовывать двоичные значения (по основанию 2) в десятичные (по основанию 10). Пользователь должен ввести число в двоичном виде как строку, а программа - преобразовать его посимвольно в десятичный вид и вывести на экран с соответствующим сообщением.
"""



"""
Атрибуты модуля
    Методы:
        two_in_ten(two_int, two_float) - Преобразует двоичные значения в десятичные.  
        delit(two_input) - Разделяет двоичное число на части до запятой и после запятой.
        main() - Обеспечивает интерфейс при преобразовании двоичных значений в десятичные.  
  
    Константы:  
        HELLO: str - текстовая строка с назначением программы.   
"""  
  

HELLO = "Программа переводит двоичные значения в десятичные."  
  
  
def two_in_ten(two_int: str, two_float: str) -> str:  
    """  
    Преобразует двоичные значения в десятичные.  
  
    Параметры метода:  
        two_int: str - часть двоичного числа до запятой.  
        two_float: str - часть двоичного числа после запятой.  
          
    Переменные метода:  
        two_int_itog: int - число из целой части переведенное в десятичную систему.  
        two_float_itog: int - число из дробной части переведенное в десятичную систему.  
  
    Возврат:  
        itog: str - Десятичное значение.
    """  

    two_int_itog = 0  
    two_float_itog = 0  
 
      
    for i in range(len(two_int)):  
        two_int_itog += int(two_int[i]) * 2 ** i  
      
    if two_float != '0':  
        for i in range(1, 5):  
            two_float_itog += int(two_float[i-1]) * 2 ** (-i)  

    else:  
        two_float_itog = 0  
          
    itog = str(two_int_itog + two_float_itog) 
      
    return itog  
  
def delit(two_input: str) -> str:  
    """  
    Разделяет двоичное число на части до запятой и после запятой.  
      
    Параметры метода:  
        two_input: str - строка двоичных значений введенных пользователем.  
          
    Переменные метода:  
        two_int: str - часть двоичного числа до запятой.  
        two_float: str - часть двоичного числа после запятой.  

    Возврат:   
        result: str - десятичное значение.  
    """  

    if '.' in two_input:  
        two_input = str(two_input).split('.')  
        two_int = two_input[0][::-1]  
        two_float = two_input[1]  
    else:  
        two_int = two_input[::-1]  
        two_float = '0'  
          
    result = two_in_ten(two_int, two_float)  
      
    return result  
  
  
def main():  
    """  
    Обеспечивает интерфейс при преобразовании двоичных значений в десятичные.  
  
    Переменные метода:  
        two_input: str - строка двоичных значений введённых пользователем.  
        result: int - десятичное значение.  
    """  
  
    print(HELLO)  
 
    two_input = input("Введите двоичное значение: ")  

    if '-' in two_input:
        two_input = two_input[1:]
        result = '-' + delit(two_input)
    else:
        result = delit(two_input)  
     
    print("Десятичное значение:", result)  
  
main()
