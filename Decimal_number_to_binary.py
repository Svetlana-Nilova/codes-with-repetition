"""
Задание.

Напишите программу, которая будет преобразовывать десятичные значения (по основанию 10) в двоичные (по основанию 2). Запросите целое число у пользователя и, следуя алгоритму, приведенному ниже, преобразуйте его в двоичную запись. По завершении выполнения программы в переменной result должно оказаться двоичное представление исходного числа. Выведите результат на экран с соответствующим сообщением. 
"""



"""  
Атрибуты модуля  
    Методы:  
        ten_in_two(ten0, ten1) - Преобразует десятичные значения в двоичные.  
        def delit(a) - Разделяет число на целую и дробную части.  
        main() - Обеспечивает интерфейс при преобразовании десятичных значений в двоичные.  
  
    Константы:  
        HELLO: str -str - текстовая строка с назначением программы.   
"""  
  
  
HELLO = "Программа переводит десятичные значения в двоичные."  
  
  
def ten_in_two(ten0: int, ten1: int) -> str:  
    """  
    Преобразует десятичные значения в двоичные.  
  
    Параметры метода:  
        ten0: int - целое десятичное число до точки.  
        ten1: int - целая часть десятичного числа после точки.  
  
    Переменные метода:  
        remnant: int - число из целой десятичной части переведенное в двоичную систему.  
        remnant1: int - число из дробной десятичной части переведенное в двоичную систему.  
        result: str - строка переведенного целого числа в двоичную систему.  
        result1: str - строка переведенного дробного числа в двоичную систему.  
        result_limit: str - строка переведенного дробного числа в двоичную систему в ограничении 4 чисел.  
        count_stop: int - число для остановки бесконечного цикла.  
      
    Возврат:  
        two: str - число введенное пользователем переведенное в двоичную систему.  
    """  
      
    result = ''  
    remnant = 0  
    result1 = ''  
    remnant1 = 0  
    count_stop = 0  
      
    while count_stop != 12 and ten1 < 2 and ten1 != 1.0:  
          
        ten1 = ten1 * 2  
          
        if ten1 > 1:  
            ten1 -= 1  
            remnant1 = 1  
            result1 = str(remnant1) + result1  
        elif ten1 == 1.0:  
            remnant1 = 1  
            result1 = str(remnant1) + result1  
        else:  
            remnant1 = 0  
            result1 = str(remnant1) + result1  
              
        count_stop += 1  
      
    result1 = str(result1[::-1])  
      
    while ten0 > 0:  
        remnant = ten0 % 2  
        result = str(remnant) + result  
        ten0 = ten0 // 2  
          
    if int(result1) == 0:  
        result_limit = ''  

    else:  
        result_limit = '.'  
        
        for i in range(4):  
            result_limit += result1[i]  
  
    two = str(result) + result_limit  

    return two  
  
def delit(ten_input: str) -> str:  
    """  
    Разделяет число на части до запятой и после запятой.  
      
    Параметры метода:  
        ten_input: float - число введенное пользователем.  
      
    Переменные метода:  
        ten_list: list - список целой и дробной части числа.  
        ten0: int - целое десятичное число до точки.  
        ten1: int - целая часть десятичного числа после точки.  
        delit_int: int - необходимое число для преобразования ten1 из целого в дробное.  
          
    Возврат:  
        result: str - число введенное пользователем переведенное в двоичную систему.  
    """  
    ten_list = ten_input.split('.')  
    ten0 = int(ten_list[0])  
    delit_int = 1  
 
    if len(ten_list) > 1: 
        for i in range(len(ten_list[1])):  
            delit_int *= 10  
            i += 1 
 
        ten1 = int(ten_list[1]) / delit_int 
        
    else: 
        ten1 = 0 
      
    result = ten_in_two(ten0, ten1)  
      
    return result  
          
  
def main():  
    """  
    Обеспечивает интерфейс при преобразовании десятичных значений в двоичные.  
  
    Переменные метода:  
        ten_input: str - строка десятичных значений введённых пользователем.  
        two: str - двоичное значение для преобразования в отрицательное значение.
        result: str - двоичное значение.  
    """  
  
    print(HELLO)  
  
    ten_input = input("Введите десятичное значение: ") 
      
    if ten_input == '0':  
        result = '0' 
        
    elif "-" in ten_input: 
        ten_input = ten_input[1:] 
        two = delit(ten_input)
        two = str(two).replace('1', '2') 
        two = two.replace('0', '1') 
        result = "1|" + two.replace('2', '0')
        
    else:  
        result = "0|"+ delit(ten_input)  
    
    print("Двоичное значение:", result)   
  

main()
