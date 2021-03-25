"""
Напишите программу-калькулятор, которая:
в первой строке считывает число (начальный результат);
в последующих строках считывает символ мат. операции и число, применяет операцию к результату;
как только прочитан символ «=», выводит результат и завершает работу.
* Программа должна обрабатывать некорректный ввод.
try:

    while stroka[0] != '=':"""
try:
        pervoe = float(input())
        while True:
            dalee = input()
            if dalee == '=':
                print(pervoe)
                break
            if dalee in ('+', '-', '*', '/', '**', '//', '%'):
                x = float(input())
                if dalee == '+':
                    pervoe =pervoe + x
                elif dalee == '-':
                    pervoe -= x
                elif dalee == '**':
                    pervoe **= x
                elif dalee == '*':
                    pervoe *= x
                elif dalee == '//':
                    pervoe //= x
                elif dalee == '%':
                    pervoe %= x
                elif dalee == '/':
                    pervoe /= x
            else:
                raise Exception
except ValueError:
        print("Это не число!")
except ZeroDivisionError:
        print("Нельзя делить на ноль")
except Exception:
        print("Некорректный ввод!")





