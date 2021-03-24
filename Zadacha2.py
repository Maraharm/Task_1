"""
Подсчет гласных.Напишите программу, которая:
считывает текст на английском языке;подсчитывает, сколько раз в тексте встречается каждая гласная буква(a, o, u, i, e, y).
Пример:
abracadabra
a 5, o 0, u 0, i 0, e 0, y 0
"""
stroka = str(input())
#string = "aaabbaacdeef"
print("a ",stroka.count('a'))
print("o ",stroka.count('o'))
print("u ",stroka.count('u'))
print("i ",stroka.count('i'))
print("e ",stroka.count('e'))# r
print("y ",stroka.count('y'))# eturns the count of 'a' in string