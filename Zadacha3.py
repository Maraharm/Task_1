"""
Напишите программу-калькулятор, которая:
в первой строке считывает число (начальный результат);
в последующих строках считывает символ мат. операции и число, применяет операцию к результату;
как только прочитан символ «=», выводит результат и завершает работу.
* Программа должна обрабатывать некорректный ввод.
try:

    while stroka[0] != '=':"""
try:
        flag = True
        pervoe = float(input())
        while flag == True:
            dalee = input()
            str1 = dalee[0]
            str2 = dalee[0:1]
            if str2 == "**":
                str3 = dalee[2:]
                pervoe = pervoe + int(str3)
                print(pervoe)
            elif str1 == '-':
                str3 = dalee[1:]
                pervoe = pervoe - int(str3)
            elif str1 == '/':
                str3 = dalee[1:]
                pervoe = pervoe / int(str3)
            elif str1 == "*":
                str3 = dalee[1:]
                pervoe = pervoe * int(str3)
            elif dalee.count("*") == 1:
                pervoe = pervoe * int(dalee[2:])
            elif "=" in dalee:
                flag = False
                print(pervoe)
                break

except ValueError:
        print("Это не число!")
except ZeroDivisionError:
        print("Нельзя делить на ноль")
#except Exception:
        print("Некорректный ввод!")





