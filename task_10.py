# ЗАДАЧА 10: Функции - усложнённая версия
#
# 1. Напиши функцию с именем calculate, которая принимает 
#    ТРИ параметра: a, b и operation (строка "plus" или "minus")
# 2. Внутри функции используй if / else:
#    - если operation равно "plus" , то верни a + b
#    - если operation равно "minus" , то верни a - b
# 3. Вызови функцию calculate ДВА раза с разными значениями 
#    и разными operation
# 4. Выведи оба результата на экран
des calculate(a, b operation)
    if operation == "plus":
        return a + b
    else:
        return a - b
result1 = calculate(10, 5, "plus")
result2 = calculate(20, 7, "minus")
print(result1)
print(result2)